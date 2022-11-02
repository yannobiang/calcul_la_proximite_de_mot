cos = torch.nn.CosineSimilarity(dim=1)
cos(u.mean(axis=1), v.mean(axis=1)) 


# cammeBert_embedding = Tranformerswordembedding('Bertbase-multiligual-case')
# cammeBert_embedding.embed('word')
# all tensor of the sentence
# word.embedding

## calcul de distance entre les deux tensor
## bert_distance = distance(np.array(word1.embedding),
##                            np.array(word2.embedding))
