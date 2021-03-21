# Exploring distributional similarity in Twitter by using multiple word embedding methods
In this prject we compare and evaluate two simple embedding models which can be constructed directly from a given co-occurrence matrix extracted from Twitter data; Positive Pointwise Mutual Information (PPMI), and Hellinger Principal Component Analysis (H-PCA). For each embedding model we consider three alternative metrics for word similarity: cosine, euclidean and manhattan distance. 

Then, taking each combination of embedding model and similarity measure, we report results of two intrinsic evaluation measures, word similarity and concept categorization, on goldstandard datasets. We then qualitatively compare hierarchicalclustering dendrograms produced by the two most promising methods on sets of concept-categorized words, finding that the resulting dendrograms reproduce sensible semantic segmentations under both embedding types. [click here](https://github.com/federicoarenasl/Evaluating-w-Embeddings/blob/main/Evaluating_Word_Embbeddings.pdf) for the full project report.
 
 ## A sneak peak at some results
Of the metrics we tested, we consistently found that for each embedding model, the best performing was cosine similarity. Additionally we found that PPMI embeddings outperformed H-PCA embeddings under cosine similarity in both the word similarity and concept categorization quantitative tests.

<p align="center">
<img  src="plots/H-PCA_dist_semantics.png" width="300">
<img  src="plots/PPMI_dist_semantics.png" width="300">
</p>

And furthermore, in hierarchical clustering tests, we found that PPMI embeddings produced more semantically homogeneous clusters.

<p align="center">
<img  src="plots/PPMI_dendrogram.png" width="400">
<img  src="plots/H-PCA_dendrogram.png" width="400">
</p>

Although we found that the PPMI word embedding outperformed
H-PCA in our results, the differences are marginal which is understandable given that both embeddings were drawn from the same numerical representation (a co-occurrence matrix).
