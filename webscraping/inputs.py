from pathlib import Path
parent_folder = Path(r"C:\Users\nicon\OneDrive\Documents\Uni - TUM\Semester2\IDP\sorted directory")
all_pdfs_path = parent_folder / "webscraping" / "all_pdf_files"

# PLEASE NOTE
# x_start_from and x_end_at begin with 0. With this logic, x_end_at is the final page which should not be included.

# 1. WEBSCRAPING:

# NASA Inputs:
nasa_url = "https://pds.nasa.gov/datasearch/ds-status/dsidStatus.jsp?nodename=ALL&col1=di.dsid&col2=di.archivestat&col3=dn.nodeid&col4=dm.msnname&col5=ii.instname&sort1=di.dsid&sort2=&sort3=&sort4=&sort5=&sortOpt1=dm.msnname&sortOpt2=ii.instname&sortOpt3=&sortOpt4=&sortOpt5=&Go=Submit"

# ESA Inputs:
esa_url = "https://www.cosmos.esa.int/web/psa/missions"

# Skyrocket Inputs:
skyrocket_primary_url = "https://space.skyrocket.de"
skyrocket_platform_url = f"{skyrocket_primary_url}/directories/sat_bus.htm"

# EOP Portal Inputs:
eop_primary_url = "https://www.eoportal.org"
eop_platform_url = f"{eop_primary_url}/satellite-missions"


# 2. PDF SCRAPING

# SMAD Inputs:
smad_path = Path(r"C:\Users\nicon\OneDrive\Documents\Uni - TUM\Semester2\SCD\SMAD.pdf")
smad_header_pattern = r"^\n?\d+\s\w.*\d+\.\d+\s\n"
smad_chapter_pattern = "C[hb]apter\s?[0-9S][0-9]? \n[A-Z].*\n"
smad_source = "smad"
smad_start_from = 9
smad_end_at = 454

# High-performance Chirped Microwave Generator for Space Applications Inputs:
pdf_118522V_path = all_pdfs_path / "118522V.pdf"
pdf_118522V_header_pattern = r"\nICSO 2020 \nInternational Conference on Space Optics\nVirtual Conference \n30 March-2 April 2021Proc. of SPIE Vol. 11852  118522V-[0-9]+Downloaded From: https://www.spiedigitallibrary.org/conference-proceedings-of-spie on 03 Aug 2023\nTerms of Use: https://www.spiedigitallibrary.org/terms-of-use"
pdf_118522V_chapter_pattern = r"\n\s*\d*\.?\s?[A-Z\s]*[A-Z]+\s*\n"
pdf_118522V_source = "High-performance Chirped Microwave Generator for Space Applications"
pdf_118522V_start_from = 2
pdf_118522V_end_at = 9

# Nonlinear Mixing Model of Mixed Pixels in Remote Sensing Satellite Images Taking Into Account Landscape Inputs:
rssi_path = all_pdfs_path / "Remote_Sensing_Satellite_Images.pdf"
rssi_header_pattern = r"\(IJACSA\) International Journal of Advanced Computer Science and Applications,  \nVol. 4, No.1, 2013  \n10[0-9] \| P a g e  \nwww. ijacsa .thesai.org  "
rssi_chapter_pattern = pattern = r"\nAbstract—|\nI*\.?\s*[A-Z]+\s+\n|\n References  \n|\nII. PROPOSED NONLINEAR MIXING MODEL OF MIXED \nPIXELS IN REMOTE SENSING SATELLITE IMAGES  \n"
rssi_source = "Nonlinear Mixing Model of Mixed Pixels in Remote Sensing Satellite Images Taking Into Account Landscape"

# Chip-Scaled Ka-Band Photonic Linearly Chirped Microwave Waveform Generator Inputs:
fphy_path = all_pdfs_path / "fphy-10-785650.pdf"
fphy_header_pattern = r"\nFrontiers.*[0-9]+(?:ORIGINAL RESEARCH\npublished: 12 April 2022\ndoi: 10.3389/fphy.2022.785650|Brunetti et al. Chip-Scaled Ka Band LCMWG)"
fphy_chapter_pattern = r"\n(?:[A-Z][A-Z]+\s*)+\n"
fphy_source = "Chip-Scaled Ka-Band Photonic Linearly Chirped Microwave Waveform Generator"
fphy_start_from = 0
fphy_end_at = 11

# Monte Carlo Ray Tracing Based Non-Linear Mixture Model of Mixed Pixels in Earth Observation Satellite Imagery Data Inputs:
mcrt_path = all_pdfs_path / "monte_carlo_nonlin.pdf"
mcrt_header_pattern = r"^\(IJACSA\).*\n.*\n\s\n.*\n.*org\s+"
mcrt_chapter_pattern = "\nAbstract—|\n[IV]+\.\s+(?:[A-Z][A-Z]+|[\w\s-]+)\s*\n|\n[A-Z][A-Z]+\s+\n"
mcrt_source = "Monte Carlo Ray Tracing Based Non-Linear Mixture Model of Mixed Pixels in Earth Observation Satellite Imagery Data"

# Radiometric and Spectral Onboard Calibration Concepts of Hyperspectral Sensors - Specifics of EnMAP and DESIS Inputs:
rscal_path = all_pdfs_path / "Whispers-Abstract-Harald-Krawczyk_BG_EC_et_al_FINAL.pdf"
rscal_source = "Radiometric and Spectral Onboard Calibration Concepts of Hyperspectral Sensors - Specifics of EnMAP and DESIS"

# Initial ground-based thermospheric windn measurements using Doppler asymmetric spatialn heterodyne spectroscopy (DASH) Inputs:
dash_path = all_pdfs_path / "oe-18-26-27416.pdf"
dash_header_pattern = r"\n.*\n.*\n.*\n.*[0-9]*$"
dash_chapter_pattern = r"\n[0-9]\.\s[a-zA-Z\s]+\n|\n3\.\s[a-zA-Z-|\s]+\n|^\s+4\..*\n"
dash_source = "Initial ground-based thermospheric windn measurements using Doppler asymmetric spatialn heterodyne spectroscopy (DASH)"
dash_start_from = 1
dash_end_at = -1

# The Ionospheric Connection Explorer Mission: Mission Goals and Design Inputs:
ioncon_path = all_pdfs_path / "Immel-ICON Mission.pdf"
ioncon_header_pattern = r"^.*T.J.\sImmel et al\.|^.*Page [0-9]+ of 36 13"
ioncon_chapter_pattern = r"[0-9][A-Z](?:\s[a-zA-Z]){3,}|2 ICON.*Objectives|3 Science Requirements"
ioncon_source = "The Ionospheric Connection Explorer Mission: Mission Goals and Design"
ioncon_start_from = 1
ioncon_end_at = 33

# Michelson Interferometer for Global High-resolution Thermospheric Imaging (MIGHTI): Instrument Design and Calibration Inputs:
mighti_path = all_pdfs_path / "nihms977423.pdf"
mighti_header_pattern = r"Englert.*\n.*\n.*Manuscript$|\n\* christoph.englert(?:.*\n){6}.*Manuscript$"
mighti_chapter_pattern = r"\n(Abstract|Acknowledgments|[1-8]\.?(?:\s[A-Za-z]+)+|7 MIGHTI Level 1 Data Product)\n"
mighti_source = "Michelson Interferometer for Global High-resolution Thermospheric Imaging (MIGHTI): Instrument Design and Calibration"
mighti_start_from = 0
mighti_end_at = 22

# A comparison of Imaging Fourier Transform with Grating Spectrometry for Tridimensional Spectroscopy Inputs:
compfourgrat_path = all_pdfs_path / "div-class-title-a-comparison-of-imaging-fourier-transform-with-grating-spectrometry-for-tridimensional-spectroscopy-div.pdf"
compfourgrat_header_pattern = r"^.*\n| \n.*Press$"
compfourgrat_chapter_pattern = r"\n(Abstract.|[1-4]\.(?:\s[A-Za-z]+)+\s\n|3. Relative signal-to-noise ratios \n)"
compfourgrat_source = "A comparison of Imaging Fourier Transform with Grating Spectrometry for Tridimensional Spectroscopy"

# Solar Imaging Spectroscopy: Multichannel Subtractive Double Pass Instruments Inputs:
solspec_path = all_pdfs_path / "div-class-title-solar-imaging-spectroscopy-multichannel-subtractive-double-pass-instruments-div.pdf"
solspec_header_pattern = r"^.*\n| \n.*Press$"
solspec_chapter_pattern = r"\n(Abstract.|[2-4]\.(?:\s[A-Za-z]+)+\s\n|1. 3D-Spectroscopy(?:\s[A-Za-z]+)+\s\n)"
solspec_source = "Solar Imaging Spectroscopy: Multichannel Subtractive Double Pass Instruments"

# Low Radio Frequency Observations from the Moon Enabled by NASA Landed Payload Missions Inputs:
lrfobs_path = all_pdfs_path / "2102.02331.pdf"
lrfobs_header_pattern = r"^[0-9]*\s\n|\n\s\n[0-9]+\s.*(?:\n.*)*$"
lrfobs_chapter_pattern = r"\n\s\n(?:Abstract|Acknowledgments)|1\.\sIntroduction\s\n|\n[2-5]\.\s[TLS].*"
lrfobs_source = "Low Radio Frequency Observations from the Moon Enabled by NASA Landed Payload Missions"
lrfobs_start_from = 0
lrfobs_end_at = 23

# # ESA’S ASTEROID IMPACT MISSION: MISSION ANALYSIS AND PAYLOAD OPERATIONS STATE OF THE ART Inputs:
astimpact_path = all_pdfs_path / "ESAs_Asteroid_Impact_Mission_Mission_Ana.pdf"
astimpact_header_pattern = r"rje" # Dummy as there is no header / footer.
astimpact_chapter_pattern =r"\n(ABSTRACT|[1-5]\.\s.*)\n" 
astimpact_source = "ESA’S ASTEROID IMPACT MISSION: MISSION ANALYSIS AND PAYLOAD OPERATIONS STATE OF THE ART"
astimpact_start_from = 0
astimpact_end_at = -1

# # The SuperCam Instrument Suite on the Mars 2020 Rover: Science Objectives and Mast-Unit Description Inputs:
supercam_path = all_pdfs_path / "supercam.pdf"
supercam_header_pattern = r"^.*|(?:\n[0-9]+[A-Z].*)+"
supercam_chapter_pattern = r"\n[1-5]\s[A-Z].*"
supercam_source = "The SuperCam Instrument Suite on the Mars 2020 Rover: Science Objectives and Mast-Unit Description"
supercam_start_from = 1
supercam_end_at = 101

# # A PROSPECTIVE UKRAINIAN LUNAR ORBITER MISSION: OBJECTIVES AND SCIENTIFIC PAYLOAD Inputs:
ukrlunorb_path = all_pdfs_path / "UKRAINIAN LUNAR ORBITER MISSION.pdf"
ukrlunorb_header_pattern = r"^.*Yu. G. Shkuratov et al.|Lunar and Planetary Science XXXIII \(2002\)\n1234.pdf\n$"
ukrlunorb_chapter_pattern = r"\n[ISPC][a-z]{6,}(?:\s[a-z]+.\n|:|\n)"
ukrlunorb_source = "A PROSPECTIVE UKRAINIAN LUNAR ORBITER MISSION: OBJECTIVES AND SCIENTIFIC PAYLOAD"

# # The Lyman-alpha Solar Telescope (LST) for the ASO-S mission — I. Scientific objectives and overview Inputs:
lst_path = all_pdfs_path / "Li_2019_Res._Astron._Astrophys._19_158.pdf"
lst_header_pattern = r"^RAA.*(?:\n.*){4}|^158.*|^H.*"
lst_chapter_pattern = r"\n(:?Abstract|[1-5]\s[A-Z\s]{3,})"
lst_source = "The Lyman-alpha Solar Telescope (LST) for the ASO-S mission — I. Scientific objectives and overview"
lst_start_from = 1
lst_end_at = -1

# # Comparison of ICON/MIGHTI and TIMED/TIDI Neutral Wind Measurements in the Lower Thermosphere Inputs:
iconmighti_path = all_pdfs_path / "jgra56871_am.pdf"
iconmighti_header_pattern = r"^.*(?:\n.*){7}|[1-9]{2,3}(?=\n)"
iconmighti_chapter_pattern = r"\n(Abstract|[1-5]\s[A-Z](?:[A-Za-z\s]+))"
iconmighti_source = "Comparison of ICON/MIGHTI and TIMED/TIDI Neutral Wind Measurements in the Lower Thermosphere"
iconmighti_start_from = 1
iconmighti_end_at = 18

# # Overview of the POLAR mission Inputs:
polmiss_path = all_pdfs_path / "ICRC2019_605.pdf"
polmiss_header_pattern = r"^.*|[1-6]$"
polmiss_chapter_pattern = r"\n[1-5]\.\s[A-Z].*"
polmiss_source = "Overview of the POLAR mission"
polmiss_start_from = 1
polmiss_end_at = -1

# # Time-resolved GRB polarization with POLAR and GBM. Simultaneous spectral and polarization analysis with synchrotron emission Inputs:
grb_path = all_pdfs_path / "1901.04719.pdf"
grb_header_pattern = r"^A.*|^J.*|A.*$"
grb_chapter_pattern = r"\n(ABSTRACT(?=\n)|[1-6]\.\s[A-Za-z]+.*(?=\n))"
grb_source = "Time-resolved GRB polarization with POLAR and GBM. Simultaneous spectral and polarization analysis with synchrotron emission"
grb_start_from = 0
grb_end_at = 10

# # PROMPT EMISSION POLARIMETRY OF GAMMA RAY BURSTS WITH ASTROSAT CZT-IMAGER Inputs:
astrosat_path = all_pdfs_path / "1707.06595.pdf"
astrosat_header_pattern = r"^.*"
astrosat_chapter_pattern = r"\n(ABSTRACT(?=\n)|[1-5]\.[A-Z\s\:]{3,})\n"
astrosat_source = "PROMPT EMISSION POLARIMETRY OF GAMMA RAY BURSTS WITH ASTROSAT CZT-IMAGER"
astrosat_start_from = 0
astrosat_end_at = 25

# # The LargE Area Burst Polarimeter (LEAP) a NASA Mission of Opportunity for the ISS Inputs:
leap_path = all_pdfs_path / "The LargE Area Burst Polarimeter (LEAP) a NASA Mission of Opportu.pdf"
leap_header_pattern = r"Proc\..*\n.*$"
leap_chapter_pattern = r"\n(ABSTRACT|ACKNOWLEDGMENTS|[1-7]\.\s[A-Z\s]*)\n"
leap_source = "The LargE Area Burst Polarimeter (LEAP) a NASA Mission of Opportunity for the ISS"
leap_start_from = 2
leap_end_at = 14

# # GRB Polarization: A Unique Probe of GRB Physics Inputs:
grbpol_path = all_pdfs_path / "2109.03286.pdf"
grbpol_header_pattern = r"^Galaxies.*|Galaxies.*$"
grbpol_chapter_pattern = r"\n(Abstract:|[1-6]\.\s[A-Za-z\s\-]+(?=\n[GMDTS])|5\. Observations|7\.\s.*)"
grbpol_source = "GRB Polarization: A Unique Probe of GRB Physics"
grbpol_start_from = 0
grbpol_end_at = 56

# # Hard X-ray polarization catalog for a 5-year sample of Gamma-Ray Bursts using AstroSat CZT-Imager Inputs:
xraypol_path = all_pdfs_path / "2207.09605.pdf"
xraypol_header_pattern = r"^.*|Corresponding author: Tanmoy Chattopadhyay\ntanmoyc@stanford.edu"
xraypol_chapter_pattern = r"\n(ABSTRACT|[1456]\.[A-Z]+(?=\n)|[23]\.[A-Z5\s]+(?=\n))"
xraypol_source = "Hard X-ray polarization catalog for a 5-year sample of Gamma-Ray Bursts using AstroSat CZT-Imager"
xraypol_start_from = 0
xraypol_end_at = 13

# # Overview of PLATO’s cameras onground and in-orbit calibration and characterisation Inputs:
platocam_path = all_pdfs_path / "1185209.pdf"
platocam_header_pattern = r"\nICSO.*(?:\n.*){4}$"
platocam_chapter_pattern = r"ABSTRACT|[1-4]\.\s[A-Z\-\s]+(?=\n)"
platocam_source = "Overview of PLATO’s cameras onground and in-orbit calibration and characterisation"
platocam_start_from = 2
platocam_end_at = 13

# # International Conference on Space Optics—ICSO 2012 - The PLATO Camera Inputs:
confplatocam_path = all_pdfs_path / "1056405.pdf"
confplatocam_header_pattern = r"ICSO.*(?:\n.*){2}$"
confplatocam_chapter_pattern = r"\nAbstract|[IV\.]{2,}\s[IPMCO][A-Z\s\.]+\n"
confplatocam_source = "International Conference on Space Optics—ICSO 2012 - The PLATO Camera"
confplatocam_start_from = 1
confplatocam_end_at = 11

# # RITA: A 1U multi-sensor Earth observation payload for the AlainSat-1 Inputs:
rita_path = all_pdfs_path / "SSEA_2022_175.pdf"
rita_header_pattern = r"^.*(?:\n.*){2}"
rita_chapter_pattern = r"\n(Abstract\s+|[1-4]\.\s[A-Z][A-Za-z\s]{,26}(?=\n))"
rita_source = "RITA: A 1U multi-sensor Earth observation payload for the AlainSat-1"

# # Store and Forward CubeSat using LoRa Technology and Private LoRaWAN-Server Inputs:
storeforw_path = all_pdfs_path / "Store and Forward CubeSat using LoRa Technology and Private LoRaW.pdf"
storeforw_header_pattern = r"^.*\n.*Conference"
storeforw_chapter_pattern = r"\n[A-Z][A-Z\s]{12,}\n|OVERVIEW.*|STORE.*|ABSTRACT"
storeforw_source = "Store and Forward CubeSat using LoRa Technology and Private LoRaWAN-Server"
storeforw_start_from = 0
storeforw_end_at = 12

# # The Flexible Microwave Payload-2: A SDR-Based GNSS-Reflectometer and L-Band Radiometer for CubeSats Inputs:
flexmicro_path = all_pdfs_path / "09044708.pdf"
flexmicro_header_pattern = r"^.*"
flexmicro_chapter_pattern = r"\n[IV]+(?:\s|\.).*|Abstract|ACKNOWLEDGMENT"
flexmicro_source = "The Flexible Microwave Payload-2: A SDR-Based GNSS-Reflectometer and L-Band Radiometer for CubeSats"
flexmicro_start_from = 0
flexmicro_end_at = 12

# # The CaNOP Cubesat Mission, Remote Imaging of the Rain Forest And Testing AI Based Identification Tools Inputs:
canop_path = all_pdfs_path / "The CaNOP Cubesat Mission Remote Imaging of the Rain Forest And.pdf"
canop_header_pattern = r"^.*\n.*(?:V\-06|Conference)"
canop_chapter_pattern = r"\n[A-Z][A-Z\s]{6,}(?=\n)|MISSION.*|LINKSTAR SYSTEM"
canop_source = "The CaNOP Cubesat Mission, Remote Imaging of the Rain Forest And Testing AI Based Identification Tools"
canop_start_from = 0
canop_end_at = -1

# # The SMOS Mission: New Tool for Monitoring Key Elements of the Global Water Cycle Inputs:
smos_path = all_pdfs_path / "8065.pdf"
smos_header_pattern = r"Kerr et al.*(?:\n.*){2}|Manuscript received.*(?:\n.*)*$"
smos_chapter_pattern = r"^[I]+\..*(?:\n[A-Z\s]+)?(?=\n)|[IV]+\.[A-Z\s]*(?=\n)"
smos_source = "The SMOS Mission: New Tool for Monitoring Key Elements of the Global Water Cycle"
smos_start_from = 0
smos_end_at = 16

# # The Soil Moisture Active Passive (SMAP) Mission Inputs:
smap_path = all_pdfs_path / "Entekhabi_The soil.pdf"
smap_header_pattern = r"\nREFERENCES(?:\n.*)*$|Manuscript.*(?:\n.*)*$|Entekhabi.*\n.*$"
smap_chapter_pattern = r"[IV]+\.[A-Z\s]+(?=\n)|ABSTRACT"
smap_source = "The Soil Moisture Active Passive (SMAP) Mission"
smap_start_from = 1
smap_end_at = 13
