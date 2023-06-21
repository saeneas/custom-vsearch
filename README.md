# custom-vsearch
minimal gpu custom embedded endpoint for weaviate vectorsearch with [multi-qa-MiniLM-L6-cos-v1](https://huggingface.co/sentence-transformers/multi-qa-MiniLM-L6-cos-v1)

## Vector Search on KITeGG Cluster

```
conda create --name vsearch 
conda activate vsearch
pip install "fastapi[all]"
conda install -c conda-forge sentence-transformers
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
```
 
 this will take a while...

```
git clone https://github.com/saeneas/custom-vsearch.git
cd custom-vsearch
uvicorn main:app --reload
```

Query with 
```
curl localhost:8000/vectors/ -H "Content-Type: application/json" -d '{"text":"give me vecs"}'
```
