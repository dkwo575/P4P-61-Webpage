# Function to update or add the data by farm ID, building ID, and data date
def update_or_add_data(data, farm_id, building_id, data_date, new_data):
    for farm in data:
        if farm["id"] == farm_id:
            for building in farm["buildings"]:
                if building["id"] == building_id:
                    for existing_data in building["data"]:
                        if existing_data["date"] == data_date:
                            existing_data.update(new_data)
                            return True
                    # If data date not found, add a new data entry
                    new_data_entry = {"date": data_date}
                    new_data_entry.update(new_data)
                    building["data"].append(new_data_entry)
                    return True
            # If building ID not found, add a new building with the data
            building_data = {
                "id": building_id,
                "buildingName": "",  # Empty building name since it's not specified
                "events": [],
                "environment": [],
                "data": [
                    {
                        "date": data_date,
                        "area": 0,  # Assuming default values for other fields
                        "fruitlets": 0,
                        "height": 0,
                        "leaves": 0,
                        "volume": 0,
                        "width": 0
                    }
                ],
                "plots": []
            }
            farm["buildings"].append(building_data)
            return True
    # If farm ID not found, add a new farm with the building and data
    data.append({
        "id": farm_id,
        "farmName": "",  # Empty farm name since it's not specified
        "buildings": [
            {
                "id": building_id,
                "buildingName": "",  # Empty building name since it's not specified
                "events": [],
                "environment": [],
                "data": [
                    {
                        "date": data_date,
                        "area": 0,  # Assuming default values for other fields
                        "fruitlets": 0,
                        "height": 0,
                        "leaves": 0,
                        "volume": 0,
                        "width": 0
                    }
                ],
                "plots": []
            }
        ]
    })
    return True


# Function to update or add the area data by farm ID, building ID, and data date
def update_or_add_area(data, farm_id, building_id, data_date, new_area):
    for farm in data:
        if farm["id"] == farm_id:
            for building in farm["buildings"]:
                if building["id"] == building_id:
                    for existing_data in building["data"]:
                        if existing_data["date"] == data_date:
                            existing_data["area"] = new_area
                            return True
                    # If data date not found, add a new data entry
                    new_data_entry = {
                        "date": data_date,
                        "area": new_area,
                        "fruitlets": 0,  # Assuming default values for other fields
                        "height": 0,
                        "leaves": 0,
                        "volume": 0,
                        "width": 0
                    }
                    building["data"].append(new_data_entry)
                    return True
            # If building ID not found, add a new building with the data
            building_data = {
                "id": building_id,
                "buildingName": "",  # Empty building name since it's not specified
                "events": [],
                "environment": [],
                "data": [
                    {
                        "date": data_date,
                        "area": new_area,
                        "fruitlets": 0,  # Assuming default values for other fields
                        "height": 0,
                        "leaves": 0,
                        "volume": 0,
                        "width": 0
                    }
                ],
                "plots": []
            }
            farm["buildings"].append(building_data)
            return True
    # If farm ID not found, add a new farm with the building and data
    data.append({
        "id": farm_id,
        "farmName": "",  # Empty farm name since it's not specified
        "buildings": [
            {
                "id": building_id,
                "buildingName": "",  # Empty building name since it's not specified
                "events": [],
                "environment": [],
                "data": [
                    {
                        "date": data_date,
                        "area": new_area,
                        "fruitlets": 0,  # Assuming default values for other fields
                        "height": 0,
                        "leaves": 0,
                        "volume": 0,
                        "width": 0
                    }
                ],
                "plots": []
            }
        ]
    })
    return True


# Function to update or add the fruitlets data by farm ID, building ID, and data date
def update_or_add_fruitlets(data, farm_id, building_id, data_date, new_fruitlets):
    for farm in data:
        if farm["id"] == farm_id:
            for building in farm["buildings"]:
                if building["id"] == building_id:
                    for existing_data in building["data"]:
                        if existing_data["date"] == data_date:
                            existing_data["fruitlets"] = new_fruitlets
                            return True
                    # If data date not found, add a new data entry
                    new_data_entry = {
                        "date": data_date,
                        "area": 0,  # Assuming default values for other fields
                        "fruitlets": new_fruitlets,
                        "height": 0,
                        "leaves": 0,
                        "volume": 0,
                        "width": 0
                    }
                    building["data"].append(new_data_entry)
                    return True
            # If building ID not found, add a new building with the data
            building_data = {
                "id": building_id,
                "buildingName": "",  # Empty building name since it's not specified
                "events": [],
                "environment": [],
                "data": [
                    {
                        "date": data_date,
                        "area": 0,  # Assuming default values for other fields
                        "fruitlets": new_fruitlets,
                        "height": 0,
                        "leaves": 0,
                        "volume": 0,
                        "width": 0
                    }
                ],
                "plots": []
            }
            farm["buildings"].append(building_data)
            return True
    # If farm ID not found, add a new farm with the building and data
    data.append({
        "id": farm_id,
        "farmName": "",  # Empty farm name since it's not specified
        "buildings": [
            {
                "id": building_id,
                "buildingName": "",  # Empty building name since it's not specified
                "events": [],
                "environment": [],
                "data": [
                    {
                        "date": data_date,
                        "area": 0,  # Assuming default values for other fields
                        "fruitlets": new_fruitlets,
                        "height": 0,
                        "leaves": 0,
                        "volume": 0,
                        "width": 0
                    }
                ],
                "plots": []
            }
        ]
    })
    return True


# Function to update or add the height data by farm ID, building ID, and data date
def update_or_add_height(data, farm_id, building_id, data_date, new_height):
    for farm in data:
        if farm["id"] == farm_id:
            for building in farm["buildings"]:
                if building["id"] == building_id:
                    for existing_data in building["data"]:
                        if existing_data["date"] == data_date:
                            existing_data["height"] = new_height
                            return True
                    # If data date not found, add a new data entry
                    new_data_entry = {
                        "date": data_date,
                        "area": 0,  # Assuming default values for other fields
                        "fruitlets": 0,
                        "height": new_height,
                        "leaves": 0,
                        "volume": 0,
                        "width": 0
                    }
                    building["data"].append(new_data_entry)
                    return True
            # If building ID not found, add a new building with the data
            building_data = {
                "id": building_id,
                "buildingName": "",  # Empty building name since it's not specified
                "events": [],
                "environment": [],
                "data": [
                    {
                        "date": data_date,
                        "area": 0,  # Assuming default values for other fields
                        "fruitlets": 0,
                        "height": new_height,
                        "leaves": 0,
                        "volume": 0,
                        "width": 0
                    }
                ],
                "plots": []
            }
            farm["buildings"].append(building_data)
            return True
    # If farm ID not found, add a new farm with the building and data
    data.append({
        "id": farm_id,
        "farmName": "",  # Empty farm name since it's not specified
        "buildings": [
            {
                "id": building_id,
                "buildingName": "",  # Empty building name since it's not specified
                "events": [],
                "environment": [],
                "data": [
                    {
                        "date": data_date,
                        "area": 0,  # Assuming default values for other fields
                        "fruitlets": 0,
                        "height": new_height,
                        "leaves": 0,
                        "volume": 0,
                        "width": 0
                    }
                ],
                "plots": []
            }
        ]
    })
    return True


# Function to update or add the leaves data by farm ID, building ID, and data date
def update_or_add_leaves(data, farm_id, building_id, data_date, new_leaves):
    for farm in data:
        if farm["id"] == farm_id:
            for building in farm["buildings"]:
                if building["id"] == building_id:
                    for existing_data in building["data"]:
                        if existing_data["date"] == data_date:
                            existing_data["leaves"] = new_leaves
                            return True
                    # If data date not found, add a new data entry
                    new_data_entry = {
                        "date": data_date,
                        "area": 0,  # Assuming default values for other fields
                        "fruitlets": 0,
                        "height": 0,
                        "leaves": new_leaves,
                        "volume": 0,
                        "width": 0
                    }
                    building["data"].append(new_data_entry)
                    return True
            # If building ID not found, add a new building with the data
            building_data = {
                "id": building_id,
                "buildingName": "",  # Empty building name since it's not specified
                "events": [],
                "environment": [],
                "data": [
                    {
                        "date": data_date,
                        "area": 0,  # Assuming default values for other fields
                        "fruitlets": 0,
                        "height": 0,
                        "leaves": new_leaves,
                        "volume": 0,
                        "width": 0
                    }
                ],
                "plots": []
            }
            farm["buildings"].append(building_data)
            return True
    # If farm ID not found, add a new farm with the building and data
    data.append({
        "id": farm_id,
        "farmName": "",  # Empty farm name since it's not specified
        "buildings": [
            {
                "id": building_id,
                "buildingName": "",  # Empty building name since it's not specified
                "events": [],
                "environment": [],
                "data": [
                    {
                        "date": data_date,
                        "area": 0,  # Assuming default values for other fields
                        "fruitlets": 0,
                        "height": 0,
                        "leaves": new_leaves,
                        "volume": 0,
                        "width": 0
                    }
                ],
                "plots": []
            }
        ]
    })
    return True


# Function to update or add the volume data by farm ID, building ID, and data date
def update_or_add_volume(data, farm_id, building_id, data_date, new_volume):
    for farm in data:
        if farm["id"] == farm_id:
            for building in farm["buildings"]:
                if building["id"] == building_id:
                    for existing_data in building["data"]:
                        if existing_data["date"] == data_date:
                            existing_data["volume"] = new_volume
                            return True
                    # If data date not found, add a new data entry
                    new_data_entry = {
                        "date": data_date,
                        "area": 0,  # Assuming default values for other fields
                        "fruitlets": 0,
                        "height": 0,
                        "leaves": 0,
                        "volume": new_volume,
                        "width": 0
                    }
                    building["data"].append(new_data_entry)
                    return True
            # If building ID not found, add a new building with the data
            building_data = {
                "id": building_id,
                "buildingName": "",  # Empty building name since it's not specified
                "events": [],
                "environment": [],
                "data": [
                    {
                        "date": data_date,
                        "area": 0,  # Assuming default values for other fields
                        "fruitlets": 0,
                        "height": 0,
                        "leaves": 0,
                        "volume": new_volume,
                        "width": 0
                    }
                ],
                "plots": []
            }
            farm["buildings"].append(building_data)
            return True
    # If farm ID not found, add a new farm with the building and data
    data.append({
        "id": farm_id,
        "farmName": "",  # Empty farm name since it's not specified
        "buildings": [
            {
                "id": building_id,
                "buildingName": "",  # Empty building name since it's not specified
                "events": [],
                "environment": [],
                "data": [
                    {
                        "date": data_date,
                        "area": 0,  # Assuming default values for other fields
                        "fruitlets": 0,
                        "height": 0,
                        "leaves": 0,
                        "volume": new_volume,
                        "width": 0
                    }
                ],
                "plots": []
            }
        ]
    })
    return True


# Function to update or add the width data by farm ID, building ID, and data date
def update_or_add_width(data, farm_id, building_id, data_date, new_width):
    for farm in data:
        if farm["id"] == farm_id:
            for building in farm["buildings"]:
                if building["id"] == building_id:
                    for existing_data in building["data"]:
                        if existing_data["date"] == data_date:
                            existing_data["width"] = new_width
                            return True
                    # If data date not found, add a new data entry
                    new_data_entry = {
                        "date": data_date,
                        "area": 0,  # Assuming default values for other fields
                        "fruitlets": 0,
                        "height": 0,
                        "leaves": 0,
                        "volume": 0,
                        "width": new_width,
                    }
                    building["data"].append(new_data_entry)
                    return True
            # If building ID not found, add a new building with the data
            building_data = {
                "id": building_id,
                "buildingName": "",  # Empty building name since it's not specified
                "events": [],
                "environment": [],
                "data": [
                    {
                        "date": data_date,
                        "area": 0,  # Assuming default values for other fields
                        "fruitlets": 0,
                        "height": 0,
                        "leaves": 0,
                        "volume": 0,
                        "width": new_width,
                    }
                ],
                "plots": []
            }
            farm["buildings"].append(building_data)
            return True
    # If farm ID not found, add a new farm with the building and data
    data.append({
        "id": farm_id,
        "farmName": "",  # Empty farm name since it's not specified
        "buildings": [
            {
                "id": building_id,
                "buildingName": "",  # Empty building name since it's not specified
                "events": [],
                "environment": [],
                "data": [
                    {
                        "date": data_date,
                        "area": 0,  # Assuming default values for other fields
                        "fruitlets": 0,
                        "height": 0,
                        "leaves": 0,
                        "volume": 0,
                        "width": new_width,
                    }
                ],
                "plots": []
            }
        ]
    })
    return True