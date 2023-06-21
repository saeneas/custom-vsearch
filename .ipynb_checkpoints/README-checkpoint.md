# custom-vsearch
minimal gpu custom embedded endpoint for weaviate vectorsearch with multi-qa-MiniLM-L6-cos-v1

## Vector Search on KITeGG Cluster

 • conda create --name vsearch 
 • conda activate vsearch
 • pip install "fastapi[all]"
 • conda install -c conda-forge sentence-transformers
 • conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
 
 this will take a while...

git clone https://github.com/saeneas/custom-vsearch.git


 • uvicorn main:app --reload