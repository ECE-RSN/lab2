# Dataset Overview

## Datasets

### Stationary Occluded

- **File**: `occludedRTK.txt`
- **Reference GPS Coordinates**: (42.3372702, -71.0869305)
- **Data Collection Duration**: 5 minutes 11 seconds
- **Weather Condition**: Cloudy
- **Equipment Used**: Emlid Reach
- **RTK corrections obtained using MaCORS**

### Stationary Open

- **File**: `openRTK.txt`
- **Reference GPS Coordinates**: (42.3382544, -71.0865255)
- **Data Collection Duration**: 5 minutes 21 seconds
- **Weather Condition**: Cloudy
- **Equipment Used**: Emlid Reach
- **RTK corrections obtained using MaCORS**

### Walking Open

- **File**: `walkingRTK.txt`
- **Reference GPS Coordinates**: Start - (42.3381079, -71.0866221) | End - (42.3385825, -71.0860263)
- **Data Collection Duration**: 1 minute 15 seconds
- **Weather Condition**: Cloudy
- **Equipment Used**: Emlid Reach
- **RTK corrections obtained using MaCORS**

## Running the Datasets

To emulate RTK GPS sensor data from these datasets, use the sensor emulator. Run the emulator with the `--file` argument followed by the path to the dataset you wish to emulate. For convenience, you may also copy the `.txt` files into your `sensor_emulator` folder and run the emulator as usual. Remember to specify the dataset file you intend to emulate.



