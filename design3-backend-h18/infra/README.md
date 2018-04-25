# Loading camera settings
```bash
uvcdynctrl -L cameraMondeSettings.txt
```

# Creating training datasets
```bash
python create_dataset.py --dataset-name mydataset_name
```
This will create an unlabelled dataset. (aka raw pictures)

## (Optional) Labelling datasets
```bash
python label_dataset.py <dataset_to_be_labelled>
```
You will then be able to add data on all pictures of the dataset you created earlier. Any previous label data will be overwritten for the dataset.