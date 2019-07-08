# My cool new model

## Abstract

This is what the model uses & what it does.

## Getting Started

```bash
cd dl-model-template
python3 -m venv ./venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
mkdir dataset
```

Add your data into `dataset/`.

### Training

Start the `visdom` server.  
```bash
visdom
```

Run the project.  

```bash
python main.py --phase train
```

### Testing

```bash
python main.py --phase test --in_path xxx/xxx.jpg  --out_path ./results/
```

## Results

This is what my cool new model achieved in testing.
Here are some graphs and tables.

## References

* [Some awesome paper](www.github.com/rshwndsz)
* [Great blog](www.github.com/rshwndsz)
