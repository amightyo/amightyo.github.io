import json
import os
import sys
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


ORCID_ID = "0009-0000-8835-5292"

TOKEN_URL = "https://orcid.org/oauth/token"
API_BASE = "https://pub.orcid.org/v3.0"

JSON_OUTPUT = Path("data/orcid_publications.json")
QMD_OUTPUT = Path("generated/orcid-publications.qmd")


def request_json(url, headers=None, data=None):
    request = Request(
        url,
        headers=headers or {},
        data=data,
    )

    with urlopen(request) as response:
        return json.loads(response.read().decode("utf-8"))


def get_access_token():
    client_id = os.environ.get("ORCID_CLIENT_ID")
    client_secret = os.environ.get("ORCID_CLIENT_SECRET")

    if not client_id or not client_secret:
        print(
            "Error: ORCID_CLIENT_ID and ORCID_CLIENT_SECRET "
            "must be set as environment variables."
        )
        sys.exit(1)

    payload = urlencode(
        {
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials",
            "scope": "/read-public",
        }
    ).encode("utf-8")

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    token_data = request_json(
        TOKEN_URL,
        headers=headers,
        data=payload,
    )

    return token_data["access_token"]


def get_works(access_token):
    url = f"{API_BASE}/{ORCID_ID}/works"

    headers = {
        "Accept": "application/vnd.orcid+json",
        "Authorization": f"Bearer {access_token}",
    }

    return request_json(url, headers=headers)


def extract_publications(works_data):
    publications = []

    groups = works_data.get("group", [])

    for group in groups:
        summaries = group.get("work-summary", [])

        if not summaries:
            continue

        work = summaries[0]

        title_data = work.get("title") or {}
        title_value = title_data.get("title") or {}
        title = title_value.get("value", "Untitled")

        publication_date = work.get("publication-date") or {}
        year_data = publication_date.get("year") or {}
        year = year_data.get("value")

        work_type = work.get("type")

        journal = work.get("journal-title") or {}
        journal_title = journal.get("value")

        external_ids = work.get("external-ids") or {}
        external_id_list = external_ids.get("external-id") or []

        doi = None

        for external_id in external_id_list:
            if external_id.get("external-id-type", "").lower() == "doi":
                doi = external_id.get("external-id-value")
                break

        publications.append(
            {
                "title": title,
                "year": year,
                "type": work_type,
                "journal": journal_title,
                "doi": doi,
            }
        )

    publications.sort(
        key=lambda item: item.get("year") or "0000",
        reverse=True,
    )

    return publications


def humanize_type(work_type):
    if not work_type:
        return "Other Scholarly Work"

    labels = {
        "JOURNAL_ARTICLE": "Journal Article",
        "BOOK_CHAPTER": "Book Chapter",
        "BOOK": "Book",
        "CONFERENCE_PAPER": "Conference Paper",
        "CONFERENCE_ABSTRACT": "Conference Abstract",
        "DISSERTATION": "Dissertation",
        "REPORT": "Report",
        "OTHER": "Other Scholarly Work",
    }

    return labels.get(
        work_type,
        work_type.replace("_", " ").title(),
    )


def generate_qmd(publications):
    lines = []

    lines.append("## ORCID-Synchronized Works")
    lines.append("")
    lines.append(
        "The works below are synchronized from my public ORCID record."
    )
    lines.append("")

    current_year = None

    for publication in publications:
        year = publication.get("year") or "Year Not Available"

        if year != current_year:
            lines.append(f"### {year}")
            lines.append("")
            current_year = year

        title = publication.get("title", "Untitled")
        work_type = humanize_type(publication.get("type"))
        journal = publication.get("journal")
        doi = publication.get("doi")

        lines.append(f"**{title}**")
        lines.append("")

        details = []

        if work_type:
            details.append(work_type)

        if journal:
            details.append(f"*{journal}*")

        if details:
            lines.append(" · ".join(details))
            lines.append("")

        if doi:
            doi_url = f"https://doi.org/{doi}"
            lines.append(f"[View DOI]({doi_url})")
            lines.append("")

        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def save_outputs(publications):
    JSON_OUTPUT.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    QMD_OUTPUT.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with JSON_OUTPUT.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            publications,
            file,
            indent=2,
            ensure_ascii=False,
        )

    qmd_content = generate_qmd(publications)

    with QMD_OUTPUT.open(
        "w",
        encoding="utf-8",
    ) as file:
        file.write(qmd_content)


def main():
    print("Connecting to ORCID...")

    access_token = get_access_token()

    print(f"Retrieving works for ORCID {ORCID_ID}...")

    works_data = get_works(access_token)

    publications = extract_publications(works_data)

    save_outputs(publications)

    print(
        f"Successfully saved {len(publications)} ORCID works."
    )

    print(f"JSON: {JSON_OUTPUT}")
    print(f"Quarto: {QMD_OUTPUT}")


if __name__ == "__main__":
    main()