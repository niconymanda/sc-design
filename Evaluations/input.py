import os
from bleurt import score
from pathlib import Path

# Setting up BLEURT checkpoints
os.chdir("c:\\Users\\nicon\\bleurt")
checkpoint = "bleurt\\test_checkpoint"
scorer = score.BleurtScorer(checkpoint)

pc_path = Path(r"c:\\Users\\nicon\\OneDrive\\Documents\\Uni - TUM\\Semester2\\IDP\\sorted directory\\Pinecone")

# 1. Familiar Tests:
# Firesat from the SMAD Textbook
firesat_mission_statement = """I am wondering which instruments could be useful for the following mission statement: Because forest fires have an 
IncreaSing Impact on recreation and commerce and ever higher public visibility, the United States needs a more effective system to Identify and monitor 
them. In addition, It would be desirable (but not required) to monitor forest fires for other nations; collect statistical data on fire outbreaks, 
spread, speed, and duration; and provide other forest management data. Ultimately, the Forest Service's fire-monitoring office and rangers In the field 
will use the data. Data flow and formats must meet the needs of both groups without specialized training and must allow them to respond promptly to 
changing conditions."""

firesat_reference = """The MODIS instrument (MODerate-resolution Imaging Spectroradiometer) can automatically detect fires. The instrument has been designed 
for a comprehensive range of scientific investigations into Earth's atmosphere, oceans, and land use, therefore MODIS may be overdesigned for the FrreSat 
mission. However, the MODIS instrument represents a mature design and a sophisticated, space-based fire detection system. MODIS fire products include 
detecting the incidence of fire, its location, emitted energy, its ratio of flaring to smoldering, and the burned area."""

# Orbiting Carbon Observatory-2
oco2_mission_statement = """I am wondering which instruments could be useful for the following mission statement: The burning of fossil fuels and other human 
activities are currently adding more than 36 billion tons of carbon dioxide to the atmosphere each year, producing an unprecedented buildup in this important 
greenhouse gas. Furthermore, less than half of the carbon dioxide emitted into the atmosphere by human activities stays there. The location and identity of 
the natural 'sinks' that are absorbing the rest of this carbon dioxide are currently not well understood. Therefore, the mission should provide data to 
understand the sources of carbon dioxide emissions and how they are changing over time. The primary science objective is to collect the first space-based 
measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize its sources and sinks and quantify their 
variability over the seasonal cycle. Moreover, the mission should highlight the parts of Earth, which help remove carbon from the atmosphere. These 
measurements quantify how much carbon dioxide these sinks will be able to absorb in the future."""

oco2_reference = """In order to detect the location of carbon dioxide emissions as well as the sinks, a spectrometer, such as the OCO-2, could be employed.
The instrument is comprised of three NIR/SWIR (Near Infrared/ Short Wave Infrared) spectrometers, with two optimised for observations of atmospheric carbon 
dioxide, and another optimised for observations of atmospheric oxygen, with data applicable in studies of atmospheric composition, as well as carbon dioxide 
and oxygen distribution. The instrument images in three modes, Nadir mode, viewing directly below the spacecraft, glint mode, viewing the location where 
sunlight is directly reflected on the Earth's surface, and Target mode, viewing a specified surface target continuously."""

# 2. Unfamiliar Tests:
# Lunar Polar Exploration
lun_pol_exploration_mission_statement = """I am wondering which instruments could be useful for the following mission statement: In the last few years, the 
analysis of observational data has suggested the existence of water in the polar regions of the Moon. The objective is to obtain the data on the quantity 
and forms of the water resources present on the Moon, in order to determine the feasibility of utilizing such resources for sustainable space exploration 
activities in the future.
- Quantity: Our aim is to obtain actual data (ground truth data) regarding the quantity of water (H₂O) from in-situ observations of areas where water is 
anticipated to exist, based on the available past observational data.
- Quality: We aim to understand the distribution, conditions, form and other parameters of the lunar water resources through in-situ observations in the 
polar regions of the Moon.
Through this mission, we also seek to improve the technology needed to explore the surface of low-gravity celestial bodies in order to support future 
lunar activities. These advancements include technology for mobility, lunar night survival and mining excavation.
"""

lun_pol_exploration_reference = """In order to confirm the presence of water on the moon, investigate its quantity, its distribution on the lunar 
surface and below ground, as well as the form the water exists in, six instruments could be required:
1. Resource Investigation Water Analyzer (REIWA), which consists of the Lunar Thermogravimetric Analyzer (LTGA), which analyses the drilled samples for 
water content; Triple Reflection Reflectron (TRITON), which identifies chemical species of the volatile component in the drilled samples based on mass 
spectrometry; Aquatic Detector using Optical Resonance (ADORE), which measures the water content in the drilled samples based on cavity ring-down 
spectrometry; Sample Analysis Package (ISAP), which provides a mineralogical and elemental measurement of the drilled samples.
2. Advanced Lunar Imaging Spectrometer(ALIS), which aids H2O/OH observation of the surface and drilled regolith.
3. Neuron Spectrometer(NS), which observes Underground neutron (hydrogen) up to one meter during rover traverse.
4. Ground Penetrating Radar(GPR), which observes Underground radar up to 1.5 meter during rover traverse.
5. Exospheric Mass Spectrometer for LUPEX (EMS-L), which provides surface gas pressure and chemical species measurements.
6. Mid-Infrared Imaging Spectrometer."""