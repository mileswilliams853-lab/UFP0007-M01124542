# Home Energy Monitor - Test Plan

## Purpose
To test the functionality, calculations, validation,
saving and loading of the Home Energy Monitor.

| Test | Description | Expected Result |
|---|---|---|
| 1 | Create an appliance | Appliance object created |
| 2 | Calculate energy consumption | Correct kWh returned |
| 3 | Calculate electricity cost | Correct cost returned |
| 4 | Enter an empty appliance name | Input rejected |
| 5 | Enter negative power | Input rejected |
| 6 | Enter zero power | Input rejected |
| 7 | Enter more than 24 hours | Input rejected |
| 8 | Enter negative electricity cost | Input rejected |
| 9 | Enter invalid compressor factor | Input rejected |
| 10 | Create an air conditioner | Correct energy calculated |
| 11 | Save appliance information | CSV file created |
| 12 | Load appliance information | Saved objects recreated |

## Test Results

All 10 automated unit tests passed successfully.

The tests verified:
- Appliance creation
- Energy consumption calculations
- Electricity cost calculations
- Input validation
- Fridge compressor validation
- Air conditioner functionality