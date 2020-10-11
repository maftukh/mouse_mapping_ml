# mouse_mapping_ml

Flask app for assessing bot-likeness of mouse movements (for deployment on Heroku)

Functinality:
`/points` endpoint for POST requests:
- Listens for a bundle of 40 points (`(x, y)` mouse positions with 50ms frequency)
- Saves the bundle into a global list
- Scores the bundle on bot-likeness using a pre-trained model (`0001.model` - XGBClassifier trained in `train_model.ipynb`)
- Returns SUCCESS or FAIL depending on the score

`/points` endpoint for GET requests:
- Returns a list 
