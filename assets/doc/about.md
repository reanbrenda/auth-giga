# About Giga AI School Mapping Validator

The Giga School AI Validation Tool, developed by [Giga](https://giga.global/), leverages the power of artificial intelligence (AI) to support your efforts in mapping school locations. We utilize satellite imagery and deep learning algorithms to identify potential school buildings across countries. This tool aims to accelerate the discovery of new, previously unmapped school locations, improve the accuracy of school location data, help government stakeholders better optimize resource allocation for education initiatives.

Using this tool, you can do the following:
- **Visualize AI-predicted school locations.** The map shows the AI predictions, which you can compare against official government school data and publicly available school location information from OpenStreetMap (OSM) and Overture. Clicking on the legend items allows you to toggle subsets of the predictions on and off. For example, if you want to focus on AI-predicted school locations that do not match any of the school points in the government dataset, you can choose to hide all predictions that match with government data, by clicking `GOVERNMENT-MATCHED` under `AI MODEL` in the legend. 
- **Validate the AI-predicted school locations.** Once you've confirmed that an AI prediction is indeed a school location, you can validate the AI-predicted school location by clicking the point on the map and choosing `Validate` on the bottom left sidebar. Conversely, if the AI prediction is erroneous (e.g. the location points to a hospital), you can choose the option, `Invalidate`. On the left sidebar, you can find a link to Google Maps which you can use as a reference for validation. You may also input the name of the school if it is known. A table beneath the map also provides a list of known school names with no corresponding lat/lon information from the government to help guide the validation process. 
- **Adjust the AI prediction probability threshold.** Users have the option to change the probability threshold and control the AI predictions displayed on the map. A higher threshold will display fewer, high-confidence predictions. A lower threshold will reveal more potential school locations, with the caveat that these predictions will contain more false positives. We therefore recommend users to begin with high-probability predictions and validate in decreasing order of confidence (or probabilities). 
- **Adjust the distance threshold.** The distance threshold indicates the maximum threshold between an AI-predicted school location and a Government (or OSM/Overture) school location in order to be considered a "match". For example, a distance threshold of 250 m indicates that an AI prediction and Government school location would be considered a match if the distance between them is less than 250 m. A lower distance threshold will show fewer matches (strict) whereas a larger threshold will result in more matches (tolerant). We recommend users to start with the default distance threshold of 250 m and ajust it according to their needs.

For any questions, you may contact:
- itingzon@unicef.org
- uozturk@unicef.org
- jdoturodriguez@unicef.org