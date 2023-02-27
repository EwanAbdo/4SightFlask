
# 4Sight job search webstie

This is my senior graduation project for Hillcrest Highschool. This project is to help newly college graduates to find a job based upon their skills in their resume. How this works is that the user puts in the location they are looking to find a job, Then they upload in their resume so that the website would parse said resumeT Once the website has parsed the resume it looks for the most dominate skills in the resume and then using that information it scarpes LinkedIn and searches for jobs based upon that skill.once those jobs are found along with the location that the user picked it takes the links of said jobs and puts it in a screen so that the user can see the name of the company, the location, and the link to their LinkedIn job applicaiton.


## Authors

+ 🏡 **Principle Investigator:**[ Ewan Abdo (@EwanAbdo)][EHome] **|** 👔 [linkedin][Elinkedin] **|** [github][Egithub]

 
[Elinkedin]:https://www.linkedin.com/in/savage-ewan-677b62263/
[Egithub]:https://github.com/EwanAbdo

+ 🏡 **Mentor:**[ Mohammad Abdo (@Jimmy-INL)][mHome] **|** 👔 [linkedin][mlinkedin] **|** [researchgate][mreasearchgate] **|** [github][mgithub]

[mHome]: https://mohammadgabdo.wixsite.com/mysite
[mlinkedin]: https://www.linkedin.com/in/mohammad-abdo-a7625082/
[mreasearchgate]: https://www.researchgate.net/profile/Mohammad-Abdo
[mgithub]: https://github.com/Jimmy-INL
## Run Locally

From your terminal Clone the project

```bash
  git clone https://github.com/EwanAbdo/4SightFlask.git
```
or click on the `Code` green button and select Download ZIP

Go to the project directory and extract it where ever you like

```bash
  cd /path/to/where/you/placed/it
```

Install dependencies: from your terminal or favourate IDE (VSCode otherwise the elder of the internet will be mad at you) terminal

```bash
  pip3 install -r requirements.txt 
```

run 

```bash
  python app.py
```
You will see the website up and running. Please select a location where you want to search for jobs, it can be a city, a state, a contry, or all (city, State, Country) if you want to be specific. Next upload your resume in a PDF format and make sure you have a 'Skills' section.

For a static deployed version with lots of limitations a version is deployed at [pythonanywhere], but for the dynamic working version please follow the previous steps to run locally.

[pythonanywhere](http://4sightjobfinder.pythonanywhere.com/)

## Acknowledgements

 - This is a senior project for [Hillcrest Highschool](https://www.hillcrestknights.com/)
