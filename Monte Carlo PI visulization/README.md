# 🎯 Animated Monte Carlo Pi Estimation

A real-time, animated Python simulation that estimates the value of Pi ($\pi$) using the **Monte Carlo Method**. 

By randomly generating coordinates inside a square bounding box and checking if they fall within an inscribed unit circle, this script visually demonstrates how statistical sampling converges on the value of $\pi$.

---

## 🚀 Features

* **Dynamic Matplotlib Animation:** Uses `FuncAnimation` to plot incoming batches of random points in real time.
* **Visual Categorization:** Instantly colors points blue if they land inside the unit circle, and red if they land outside.
* **Live Calculation:** Updates the estimated $\pi$ value in the plot title with every passing frame.

---

## 📊 How the Math Works

The simulation takes advantage of a simple geometric ratio:
1. The area of a square from -1 to 1 is $2 \times 2 = 4$.
2. The area of an inscribed unit circle (radius = 1) is $\pi \times 1^2 = \pi$.
3. The ratio of the circle's area to the square's area is exactly $\frac{\pi}{4}$.

Using the Pythagorean theorem ($x^2 + y^2 \leq 1$), the script checks each random point:

$$\pi \approx 4 \times \frac{\text{Points Inside Circle}}{\text{Total Points Generated}}$$

---

## ⚙️ Configuration Parameters

The script is currently configured with the following parameters for high-volume sampling:

* **Total Points:** `1,000,000` (The total number of coordinates processed across the simulation)
* **Batch Size:** `5,000` (Points generated and plotted per frame to keep the animation progressing rapidly)
* **Interval:** `1ms` (The delay between animation frames)

---

## 🛠️ Requirements & Installation

Make sure you have the required external Python libraries installed:

```bash
pip install numpy matplotlib
