# Mrs-Deal

Mrs. Deal is an automatic poker dealer powered by an ESP32 and designed for the Northwestern University course Elec_Eng 327: Electronic System Design II: Project (Spring 2022). The design aims to make dealing in poker automated in order to make the process easier for beginners and more hands off for experienced players. 

There are three main features of Mrs. Deal. The first is the servo and DC motors that are used to point the dealer in the correct direction and send out cards. The second is ESP32-CAM that caputres an image of the cards being dealt and identifies it using computer vision. The third is a server that is set up so that people who are not playing can see who has what cards (watching a game of poker without knowing any cards is significantly more boring). 

Due to a number of complications (including the entire project group getting covid at the same time), we were unable to implement some of the features above to completion. If there was more time, we would have set up an application to hold the information from the server and ESP32-CAM for an easier interface. In addition to that, the DC motors dealing the cards could have been made to be more consistent.

Mrs. Deal: Never Miss Deal (misdeal) again. Bah dum tiss.
