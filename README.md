# Csv-Distribution-app
Simple app to gather csv files and combine them for use in Alphacam and Caldera RIP

Gather CSV files from Navision orders and combine them, adding settings, for Alpha-Cam to use.
Runs threadded to surveil folders and in the meantime clean the output from AC, for Caldera Rip to use the files directly to the printing qeue.

This is assum AC and Caldera automatic folders is configured.

The idea is AC gets the orders and nests them together for more usage of materials. But AC in itself takes evry csv that comes in all the time.
This apps is set to gather orders to give greater numbers for nesting.

Added is also a code for an AC repport and script that can gather the data and represent the different orders which are made.
