docker run --gpus all --ipc=host -v /mnt/d/LanguageTehnologies/TextRL:/textRL --workdir /textRL --ulimit memlock=-1 --ulimit stack=67108864 -it -p 8888:8888 --name pytorch --rm nvcr.io/nvidia/pytorch:23.04-py3

jupyter notebook .

cd ../sig
docker cp ./ pytorch:workspace/sig
docker cp pytorch:workspace/sig ./

https://github.com/voidful/TextRL#initialize-agent-and-environment


pip install pfrl@git+https://github.com/voidful/pfrl.git
pip install textrl

OR

pip install -e .


