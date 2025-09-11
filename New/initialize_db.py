from data_manager import create_tables, add_place
from miniprog import data  # make sure data is accessible or imported properly

def populate_sample_data():
    create_tables()
    for key, item in data.items():
        place = item.get("place", "")
        state = item.get("state", "")
        places = item.get("places", "")
        hotels = item.get("hotels", "")
        details = item.get("details", "")
        
        # You can define image path mapping here if images exist:
        # For now, we'll use a placeholder path. Replace with correct ones.
        image_path = f"images/{place.lower().replace(' ', '_')}.png"
        
        add_place(place, state, places, hotels, details, image_path)

if __name__ == "__main__":
    populate_sample_data()
    print("Database initialized and sample data added.")
    