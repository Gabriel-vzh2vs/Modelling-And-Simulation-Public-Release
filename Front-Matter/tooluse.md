# When to use a tool

An important part of any tool is using it appropriately. The following information refers to
using tools like Excel, Python, and Simulation Software when doing the work inside of this book or
outside in a professional manner.

## Excel

Excel is a great tool for specific purposes such as building toy models, basic optimization,
spreadsheets representing non-interactive data, or project management - and it is often
used outside of this context, which may cause issues in  maintenance, performance or
reliability. This subsection provides guidance in what applications are appropriate or
inappropriate for Excel.

Consider using different tools than Excel when you need to

- store data that needs to be assessed by other software or requires access control, instead use DBMSs like PostgreSQL, MariaDB.
- have speed at processing data and information, instead use programming languages like Rust, Python with Pypy, or Java.
- simulate complex systems, particularly ones with any form of Differential Equation determining their behaviors, instead use simulation software like simpy, Anylogic, SIMIO.
- analyzing big data, for reference big data is greater than 500 entities in a list, instead use programming languages with frameworks to handle it like R, Python's Dask/PySpark, Apache's Flink/Samza/Storm.

## SIMIO

## Anylogic

## SimPy
