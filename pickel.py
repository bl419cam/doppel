import pickle
import 

pipe = Pipeline([
    ('extract_deep_features', extractor),
    ('classify', forest)
])

pipe.predict('provided_photo')


with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
    
