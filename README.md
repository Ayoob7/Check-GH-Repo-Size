# Check-GH-Repo-Size
A program to check the size of a GitHub repo before cloning.


Many a time before cloning a GitHub repository we might feel the need to check their repo size. While we could use the GitHub API to get a JSON object that has the size attribute, I thought it would be very handy and convenient to developers who work with a lot of repos on a daily basis. 

### This primarily for the from the AI community and Web development community as the resources and bundled materials are always increasing in size.


## Usage

The usage is simple.

**Step 1:** Download the repo_check_size.py file

**Step 2:** *(For Linux and Mac users in terminal)* and *(For Windows users in powershell or command prompt)*

Run the following command in terminal
```
python repo_check_size.py <a GitHub repository>
```

### Example
*Directory Root*
```
python repo_check_size.py https://github.com/opencv/opencv
```
*Directory clone format*
```
python repo_check_size.py https://github.com/opencv/opencv.git
```

*Subdirectory of repo*
```
python repo_check_size.py https://github.com/opencv/opencv/tree/master/data
```

All the above would give the size of the repo.

### Usage Gallery
![alt text](https://github.com/Ayoob7/Check-GH-Repo-Size/blob/master/images/Screenshot1.png)


## Credits

Some methods based on the answer given by StackOverflow user - https://stackoverflow.com/users/2062973/james-sapam to the question posed here - https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python
