---
layout: post
coverImg: "post-bg.jpg"
title: "Implement a Gravitational Clustering Module in ECL Language"
subtitle: "TechEdge International"
author: Itauma Itauma
date: March 17, 2015
geometry: margin=1in
description: "Work in progress..."
---

## Abstract

HPCC Systems provide an open source platform for Big Data processing. The implementation of the gravitational clustering algorithm (GCA) will be done in ECL language. The implementation will be based on the fundamental law of homogeneous species. It is observed that GCA is better than other hierarchical clustering algorithms in terms of speed, robustness and how well it determines the number of clusters. This project is focused towards contributing to the ECL-ML library available on GitHub.  

## Project Description

HPCC Systems provide an open source platform for Big Data processing. It has an ECL-ML library with a few machine learning algorithms implemented. Currently, clustering algorithms such has K-Means and Agglomerative hierarchical clustering exist. From the literature, it is observed that in terms of complexity and storage, the gravitational clustering algorithm is better than agglomerative clustering algorithm. The implementation of the gravitational clustering algorithm will be done in ECL language.


## Objectives

- Implementation of the gravitational clustering algorithm in ECL.
- Take advantage of the massively parallel HPCC distributed platform.
- Run the algorithm on a single and multi-node HPCC cluster.
- Contribute to the ECL-ML library.

## Project Intuition

- The gravitational clustering algorithm is simply the basis of Life.  
- Noise is always stagnant and cannot affect that which is in constant motion unless the entity becomes noise.  
- That which is in motion would always experience the laws of gravitation which is also related to the laws of homogeneous species.  
- It is natural that homogeneous species or clusters would be attracted to each other.  

## Time-line

- 3 Months.


## Proposed Algorithm

- [The gravitational clustering algorithm according to W E Wright.][wright].
- Erik Stone gave a good presentation of [the algorithm.][algorithm].

[wright]: http://cis.missouri.edu/dm03_08GomezJ.pdf
[algorithm]: http://cis.missouri.edu/Erik.ppt

## Results

- Submitting the algorithm to the [ECL-ML github repository.][eclml].
- Comparison of the speed, robustness and how well it determines the number of clusters.

[eclml]: https://github.com/hpcc-systems/ecl-ml

## Thoughts on Implementation

- Considering the data is partitioned into 9 node clusters, one of the clusters could serve as a Master cluster which stores the statistics of other clusters locally.   
- Each cluster contains a set of data points (real data and noise).   
- There will be 2 basic constraints:  
    + Gravitational Force   
    + Distance between data points   
- Since it is an iterative algorithm, we use the loop data structure   
    + In each step, using distribute, meaning the process is applied locally on every node, we compute the distances (shared).   
    + If a data point at the border of a node has a closer distance to other data point on adjacent node, then the data point is merged to the set of data points in the other node.   
    + The Gravitational Force constraints applied locally on every node is used to exclude the noise data point from the set of data points in each node, since the gravitational point acting on it will be small.   
    + Also less data trajectory from node to node interaction is ensured since a higher gravitational force is exerted amongst the set of data points in a cluster.   
- We could also take into consideration distribution that are skewed:   
    + We apply a merge join of all set of data points on every node and compute a skew value of the merged distribution locally.   
    + If the data is skewed, then we apply a transformation on the merged set of data points to make it close to a normal distribution and then redistribute it across the 9 node clusters.   
- After the data is generated, we can use the visualization tool to construct the histogram of the data to get a better sense of how it is distributed.   