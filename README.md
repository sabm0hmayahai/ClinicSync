# ClinicSync
An automated AI based diagnosis delivery solution for the radiology domain.

# Instructions

### 1. First download the model JSON and h5 files from the below link

https://drive.google.com/drive/folders/1j6XiDT5sx1nXa_jINgpBxOOIi_TridQM?usp=sharing

### 2. Create a folder called as models inside the clinicsync directory and add the JSON and h5 files inside it.
#### The final folder structure should look like this
```python
ClinicSync
|- clinicsync
      |- inputimages
      |- models
          |- pneumonia_model.json
          |- pneumonia_model.h5
      |- static
      |- templates
      |- __init__.py
      |- utils.py
      |- views.py
|- ReadMe.md
|- requirements.txt
|- runserver.py
```

### 3. Install the required libraries

```python
pip install -r requirements.txt
```

### 4. To run the server

```python
python runserver.py
```

AGBI Digital HealthTech Grand Challenge

https://www.hackerearth.com/challenges/hackathon/agbi-digital-healthtech-grand-challenge/
