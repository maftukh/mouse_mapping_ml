# mouse_mapping_ml

Flask app for assessing bot-likeness of mouse movements (ready for deployment on Heroku)

### Functionality
`/points` endpoint for POST requests:
- Listens for a bundle of 40 points (`(x, y)` mouse positions with 50ms frequency)
- Saves the bundle into a global list
- Scores the bundle on bot-likeness using a pre-trained model (`0001.model` - XGBClassifier trained in `train_model.ipynb`)
- Returns SUCCESS or FAIL depending on the score

`/points` endpoint for GET requests:
- Returns a list of 40-point observations

### Usage
- Install requirements
- Start app.py

To check whether mouse movements are bot-like without setting up the backend, just make a POST request to https://floating-journey-29995.herokuapp.com/points with the JSON like `{'points': (40, 2)-shape array of normalized mouse positions}`

### P.S.
It is a part of a More.Tech hackathon project. Follow the links for more details on [Frontend](https://github.com/WhoAmIRUS/vtb-hackathon) and [another Backend](https://github.com/NikitaChizhov/More.Tech). Presentation could be find [here](https://drive.google.com/file/d/1VmZ4UuLaf2sDTSS21iNIhBxrvZRtXG3V/view?usp=sharing)
