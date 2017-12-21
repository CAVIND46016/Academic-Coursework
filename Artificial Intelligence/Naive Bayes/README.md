## Results

### Removal of digits, non-ascii chars and english stopwords where len(word) > 1 and all lowercase <br>
Accuracy: 65.4 % <br>

### Removal of digits, non-ascii chars, special characters and english stopwords where len(word) > 1 and all lowercase <br>
Accuracy: 66.0 % <br>

### Removal of digits, non-ascii chars, special characters and english stopwords where len(word) > 1 <br>
Accuracy: 65.8 % <br>

### Removal of digits, non-ascii chars, special characters and english stopwords where len(word) > 1 and all lowercase, porter stemmer <br>
Accuracy: 65.4 % <br>

### Removal of digits, non-ascii chars, special characters and english stopwords where len(word) > 1 and all lowercase <br>
custom_stopwords = ['job', 'hiring']; <br>
Most common words: <br>
Philadelphia,_PA: philadelphia, pa, im, amp, philly <br>
Atlanta,_GA: atlanta, ga, georgia, jobs, careerarc <br>
Boston,_MA: boston, careerarc, jobs, latest, st <br>
Toronto,_Ontario: toronto, ontario, st, trucks, b/w <br>
San_Francisco,_CA: ca, san, sanfrancisco, francisco, california <br>
Washington,_DC: dc, washington, im, careerarc, jobs <br>
San_Diego,_CA: ca, san, sandiego, diego, jobs <br>
Orlando,_FL: orlpol, orlando, opd, fl, amp <br>
Manhattan,_NY: new, york, ny, nyc, newyork <br>
Chicago,_IL: chicago, il, im, jobs, careerarc <br>
Houston,_TX: houston, tx, jobs, careerarc, latest <br>
Los_Angeles,_CA: ca, los, angeles, losangeles, jobs <br>

Accuracy: 67.0 % <br>

### Removal of digits, non-ascii chars, special characters and english stopwords where len(word) > 1 and all lowercase <br>
custom_stopwords = ['job', 'hiring', 'jobs', 'careerarc', 'latest', 'opening']; <br>
Most common words: <br>
Manhattan,_NY: new, york, ny, nyc, newyork <br>
Boston,_MA: boston, st, report, massachusetts, see <br>
Atlanta,_GA: atlanta, ga, georgia, im, amp <br>
Chicago,_IL: chicago, il, im, illinois, amp <br>
Houston,_TX: houston, tx, click, nursing, texas <br>
Philadelphia,_PA: philadelphia, pa, im, amp, philly <br>
Toronto,_Ontario: toronto, ontario, st, trucks, b/w <br>
San_Francisco,_CA: ca, san, sanfrancisco, francisco, california <br>
Washington,_DC: dc, washington, im, day, amp <br>
Los_Angeles,_CA: ca, los, angeles, losangeles, hollywood <br>
Orlando,_FL: orlpol, orlando, opd, fl, amp <br>
San_Diego,_CA: ca, san, sandiego, diego, im <br>

Accuracy: **67.19999999999999 %**
