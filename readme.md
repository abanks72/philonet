# Philonet

Philonet is a web-based application that allows you to explore the connections and influences among various philosophers throughout history. By representing these intricate networks as a graph, the project offers a visual and interactive way to gain insights into the philosophical landscape.

```diff
- WEB APP IN EARLY DEVELOPMENT - 
https://philotest-1c81b50727e1.herokuapp.com/
```
## Table of Contents

  - [Features](#features)
  - [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Local Testing](#local-testing-localtestpy-and-testhtml)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

## Features

Philonet offers a range of features to explore the connections and influences among philosophers throughout history. Some of the key features include:

- **Dynamic Visualization:** Visualize the philosopher network using D3.js, built from Python's NetworkX library, which provides an interactive and dynamic graph visualization.

- **Era-Based Filtering:** Select a specific era (All, BC, or AD) to focus on philosophers from a particular time period.

- **Weighted Edges:** Explore philosopher connections with weighted edges based on shared attributes, providing insight into the strength of influences.

- **Community Detection:** Discover communities of philosophers within the network using community detection algorithms.

- **Node and Edge Information:** View detailed information about each philosopher by hovering over nodes, and see philosopher connections through edges.

## Getting Started

To run the philosopher influence network visualization locally, follow these steps:

### Prerequisites

Make sure you have the following requirements:

- Python 3.x installed on your system.
- The `requirements.txt` file, which contains all the necessary Python packages and dependencies.

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo

2. Install the required Python packages from requirements.txt:
   
   ```bash
   pip install -r requirements.txt
   

### Local Testing (localtest.py and test.html)
The local test server will be accessible at http://localhost:5000. 

   ```bash
   python localtest.py
  ```
**Important:** The local testing environment is specifically designed for testing and development purposes. To deploy the project to a public server, consider using an appropriate hosting platform.

### Usage
- select the era from the dropdown menu to filter the philosopher influence network. You can choose from "All," "BC," or "AD."

- Interact with the visualized graph to explore the philosopher network. Hover over nodes to view philosopher names and their influences.

- Explore the detected communities within the philosopher network for a deeper understanding of shared attributes and influences.

### Contributing
If you'd like to contribute to this project, please follow our Contribution Guidelines.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
