# CZ4062-assignment

## Objectives

The main objective of this assignment is for the students to learn the greybox fuzzing testing techniques and knowledge of vulnerability issues for modern projects. After completing the assignment, students should be able to:

- Understand how fuzzing works and how to seed with the proper inputs to make fuzzing efficient;
- Reproduce the existing vulnerability bugs inside widely used open source projects.

## Problems Description

### Problem 1

A simple C program(“[problem1.c](problem1/src/problem1.c)”) that can read from a regular file is provided. This tiny program contains multiple conditions that will lead to different execution trace by seeding them with input files. Some of them are considered to be normal executions, others may require too much time to run (we consider an execution that runs more than 1s to be timeout), and the others lead to crashes. The students tasks are to discover test case files that lead to corresponding executions by using AFL fuzzer.

### Problem 2

The students are required to find Proof of Crashes (PoCs) for some widely used open source projects. You are free to use arbitrary techniques (including AFL fuzzing) to help discover and confirm the execution crashes.

The following are the CVEs in this projects:

- [CVE-2017-14039](http://www.cvedetails.com/cve/CVE-2017-14039/) ([PoC](problem2/poc_1/))
- [CVE-2017-5511](http://www.cvedetails.com/cve/CVE-2017-5511/) ([PoC](problem2/poc_2/))
- [CVE-2017-14164](http://www.cvedetails.com/cve/CVE-2017-14164/) ([PoC](problem2/poc_3/))
- [CVE-2013-2174](http://www.cvedetails.com/cve/CVE-2013-2174/) ([PoC](problem2/poc_4/))
- [CVE-2008-4225](http://www.cvedetails.com/cve/CVE-2008-4225/) ([PoC](problem2/poc_5/))
