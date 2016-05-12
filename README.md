# Paprikachips en circuits
## Door Tinka Zorge, Joëlle Zweekhorst en Leslie Dao
Heuristieken chips probleem

### Algoritme
Het A* algoritme wordt herhaaldelijk gebruikt om de paren in de netlist te verbinden met het kortst mogelijk pad.
### Gebruik
Het bestand main_complete.py probeert de netlists compleet op te lossen. Als het algoritme is ingebouwd door al gelegde draden, zal het proberen oude draden weg te halen en het pad af te maken. Verwijderde draden zullen later teruggeplaatst worden. main_complete.py zal niet in staat zijn om alle netlists compleet op te lossen. "Onoplosbare" netlists zullen benaderd worden. De bestanden hiervoor bevinden zich in de map benadering. Bij het runnen van chips.py zal het script vragen welke netlist benaderd moet worden. Voor de benadering zijn meerdere opties mogelijk. Er kan gekozen worden voor een hill climber (H), die willekeurig twee paren in de netlist van plek verwisselt, of voor random shuffle (R), die de hele netlist willekeurig husselt na elke iteratie. Daarnaast kan de netlist initieel gesorteerd worden op manhattan distance, maar dat is ook een optie die de gebruiker mag kiezen (Y/N). Na een maximum aantal iteraties, of als de netlist toch geheel oplosbaar blijkt te zijn, wordt de visualisatie aangeroepen die de draden die gelegd konden worden laat zien.

