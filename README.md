# Analysis of Average Rainfall of India
How has the Average Rainfall Rate in India (considering monthly analysis) varied over the last century? <br><br>
Region: India <br>
Domain: Weather (Rainfall Variation over a century) <br>
Duration: 1901-2015 <br>

> **Based on the Data given on data.gov.in:**
> ## Links to the Data Set
> - [Link 1]( https://drive.google.com/open?id=1IBqmzgD8iDgZZ8jXNVoYX-DE4If-dxjg )
> - [Link 1]( https://data.gov.in/resources/all-india-area-weighted-monthly-seasonal-and-annual-rainfall-mm-1901-2015 )

### Implementation of the Above Paper.
Technical platform used for implementation: **Python3, Jupyter Notebook**

> Implemented By:
> - Arpit Jain

## Abstract
This visualization was concerned with answering the question of how has the Average Rainfall Rate in India (considering monthly analysis) varied over the last century. Data Website of Indian Government (data.gov.in) was scrapped for the data concerning the average rainfall of each month for all the years of the previous century(1901-2015).
<br>
Annual Average Rainfall was obtained from Monthly Rainfall average values for each year. <br>
Similarly, average rainfall values for the phases (Seasons) were obtained. The year was divided into 4 phases - <br>
1. Jan-Feb (Winter) <br>
2. Mar-May(Spring) <br>
3. Jun-Sep(monsoon) <br>
4. Oct-Dec(Fall). <br><br>
A 100-year moving average was plotted to help the reader identify any major trends in the variation of Average Rainfall over the century.
<br><br>
The Plot is divided into three parts - 
<br>
A. Monthly Variation of Average Rainfall over the century (1901-2015) <br>
Separate Scattered Variation of the rainfall for Each month.<br>
<br>
B. Annual Average Rainfall Variation (1901-2015)<br>
A line Graph representing the variation of annual Rainfall over the years.<br>
<br>
C. Seasonal or Phase wise Rainfall Distribution (Jan-Feb, Mar-May, Jun-Sep, Oct-Dec)<br>
Scattered Representation of the relative variation of rainfall during separate Seasons.<br>
<br>
The plot indicates that the though the Average annual rainfall is more or less unpredictable and highly varying, The maximum rainfall occurs in the months of July - September (As seen by the large dots on the scatter graphs). 
<br><br>

## Cairo’s principles of truth, beauty, function, and insight.
1. Truthfulness - The data is represented as it is. No distortion of any data inputs during plotting is done. The data is properly scaled and can be compared easily. Over-Dramatic representation of data is strictly avoided. 
<br><br>
2. Beauty - The information plotted is clear to understand and uses colors which are easy to eyes. Matplotlib's Seaborn-Colorblind color theme was used to maintain the overall beauty of the graphs.
<br><br>
3. Functionality - The Plot is divided into three parts -<br>
A. Monthly Variation of Average Rainfall over the century (1901-2015)<br>
B. Annual Average Rainfall Variation (1901-2015)<br>
C. Seasonal or Phase wise Rainfall Distribution (Jan-Feb, Mar-May, Jun-Sep, Oct-Dec)<br>
<br>
4. Insightfulness - The following key points were kept in mind for delivering insightful observations.<br>
A. Color Scheme is Viridis which represented scale of average rainfall from Low(Purple) to High(Bright Yellow)<br>
B. In the Scatter Plots ( Monthly Data), The size of scattered points is kept dynamic to represent their relative measure.<br>
C. Scales and the sizes of Axes are also kept Relative for ease of representation and understanding.<br>
