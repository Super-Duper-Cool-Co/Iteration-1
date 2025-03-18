# Super Duper Cool Canadian Animal Database

## A Super Duper Cool Company Project

## Overview

This program consists of the front and back end for an HTML program that serves as a database for several species of 
fauna native to Canada.

## Setup

- TODO: Update the README.md to be up to date with current functionalities.

Opening the database is as simple as opening homepage.html, which consists of a top menu bar and a large image of 
Canada. This image currently serves as a link to the full database, but future iterations will have titles in each 
province which, when clicked, will take the user to a list of animals that can be found in that province. The top menu 
bar also features an 'Add Animal' link, which takes the user to a form on the front end of the site where they can add 
entries themselves. This form is currently not functional, in that it does not add the animal to SDCC_Database.csv, but 
the text fields, buttons and site direction do work as intended.

Any changes to the database are done by executing backend.py, which is a simple command line interface with several 
menu options for adding, removing or editing entries to the database. Once the exit command is entered, the 
program automatically rewrites list.html to update any changes.