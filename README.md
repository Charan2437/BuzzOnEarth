# EV Infrastructure Planning - BuzzOnEarth India Hackathon

## Project Overview
This project focuses on **Electric Vehicle (EV) Infrastructure Planning** in India, aiming to address the growing adoption of EVs. As India expects to have over 1 million EVs on the road by 2024, with the market projected to grow at a CAGR of 23% from 2021-2030, there is an urgent need to optimize the placement of EV charging stations.

### Team Members
- **Ramesh Babu** (22BCS208)
- **Tanvi Koranne** (22BEC123)
- **K.Charan Teja Reddy** (22BCS132)
- **Arun Jatothu** (22BCS113)
- **Dasari Venkata Sri Sai Akshay Kumar** (22BCS075)

## Problem Statement
With the rise in EV adoption, there is a critical need for **well-distributed charging stations** to ensure:
- **Convenience for EV users**
- **Minimized traffic congestion and delays**
- **Support for green energy initiatives**

Current issues include:
- Rapid urbanization
- Traffic congestion
- Pollution and inadequate waste management

## Approach: EV Station Placement
The solution uses a combination of **Reinforcement Learning (RL)** and **Machine Learning (ML) classification** to optimize EV station placement in cities. The key methodology involves:
1. **Dividing cities into grids** for manageable analysis.
2. **Applying a machine learning classifier** to each grid to predict the suitability of EV stations.
3. **Reinforcement Learning** selects and refines the grid selection process until optimal placements are identified.

### Dataset
The dataset consists of road networks, points of interest (POIs), population density, and other infrastructure details (e.g., civic buildings). The data is collected from 9 cities in Germany to predict EV station placements.

## Tech Stack
### Frontend:
- **React.js**
- **Tailwind CSS**
- **Deck.gl** (for mapping)

### Backend:
- **Python**
- **FastAPI**
- **Uvicorn**

### Machine Learning:
- **PyTorch**
- **Scikit-learn**

### Intel Optimization Tools:
- **Intel® oneAPI AI Analytics Toolkit**
- **AI Tools from Intel**
- **Intel® Xeon® Platinum 8468V**

## Results
The performance of the models is as follows:
- **Big City Model**: AUC = 0.6893, Accuracy = 81.93%
- **Small City Model**: AUC = 0.7221, Accuracy = 88.77%
- **Combined Cities Model**: AUC = 0.7319, Accuracy = 86.06%

The solution demonstrates a predictive accuracy of **70-80%**, with potential for improvement as more charging infrastructure is developed.

## Future Scope
- **Real-Time Data Integration**: Enhance predictions by incorporating dynamic data.
- **Advanced Algorithms**: Explore hybrid models to improve accuracy.
- **User Behavior Analysis**: Predict future demand by analyzing EV driver behavior patterns.

## License
This project is part of the **BuzzOnEarth India Hackathon**.
