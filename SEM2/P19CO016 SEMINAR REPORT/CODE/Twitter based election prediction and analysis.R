#install the respective packages into Rstudio(uncomment is not installed)
#install.packages("twitteR")
#install.packages("RCurl")
#install.packages("ROAuth")

#loading the packages
library(twitteR)
library(RCurl)
library(ROAuth)

#collecting the info
api_key<-"TCZ9ExykX4BzItaKseWueIpSs"
api_secret<-"1WPMZ85Cko6DtkmkUFzKpsWP0ZbmK16bmzeeYgVvYJHJeP512y"
access_token<-"3258828348-QL7t9Ej40qR9sSNaiJeJhYC8KRmJmmx3YvbFAgH"
access_token_secret<-"Yx1clNeau00XpY0h6auwN2wBY3CCtaqgkgxDRQeV7qlii"

setup_twitter_oauth(api_key,api_secret,access_token,access_token_secret)

mytweet<-searchTwitter('$narendramodi',n=1500,lang='en')
mytweet

mytweet1<-searchTwitter('$rahulgandhi',n=1500,lang='en')
mytweet1

n.tweet <- length(mytweet)
n.tweet1 <- length(mytweet1)
head(n.tweet)
head(n.tweet1)

mytweet.df<-twListToDF(mytweet)
mytweet1.df<-twListToDF(mytweet1)
head(mytweet.df$text)
head(mytweet1.df$text)

#loading the data into csv files
write.csv(mytweet.df,file='/Users/DELL/Desktop/election.csv')
write.csv(mytweet1.df,file='/Users/DELL/Desktop/election1.csv')
#head(election)
#head(election1)

# Reading the  file
election<-read.csv(file.choose(),header=T)
str(election)
election1<-read.csv(file.choose(),header=T)
str(election1)

#look over data
head(election)
head(election1)


#Building the corpus

#install the respective packages into Rstudio(uncomment is not installed)
#install.packages("tm")

#loading data into corpus
library(tm)
corpus <- iconv(election$text,to = "utf-8")
corpus <- Corpus(VectorSource(corpus))
inspect(corpus[1:1000])

library(tm)
corpus1<- iconv(election1$text, to = "utf-8")
corpus1 <- Corpus(VectorSource(corpus1))
inspect(corpus1[1:1000])


# Cleaning the text

corpus <- tm_map(corpus, tolower)
inspect(corpus[1:1000])
corpus1 <- tm_map(corpus1, tolower)
inspect(corpus1[1:1000])

corpus <- tm_map(corpus, removePunctuation)
inspect(corpus[1:1000])
corpus1 <- tm_map(corpus1, removePunctuation)
inspect(corpus1[1:1000])

corpus <- tm_map(corpus, removeNumbers)
inspect(corpus[1:1000])
corpus1 <- tm_map(corpus1, removeNumbers)
inspect(corpus1[1:1000])


cleanset <- tm_map(corpus, removeWords, stopwords('english'))
inspect(cleanset[1:1000])
cleanset1 <- tm_map(corpus1, removeWords, stopwords('english'))
inspect(cleanset1[1:1000])


removeURL <- function(x) gsub('http[[:alnum:]]*', '', x)
cleanset <- tm_map(cleanset, content_transformer(removeURL))
inspect(cleanset[1:1000])
removeURL <- function(x) gsub('http[[:alnum:]]*', '', x)
cleanset1 <- tm_map(cleanset1, content_transformer(removeURL))
inspect(cleanset1[1:1000])


cleanset <- tm_map(cleanset, stripWhitespace)
inspect(cleanset[1:1000])
cleanset1 <- tm_map(cleanset1, stripWhitespace)
inspect(cleanset1[1:1000])


# Term document matrix
tdm <- TermDocumentMatrix(cleanset)
tdm
tdm <- as.matrix(tdm)
tdm[1:10, 1:20]
tdm1 <- TermDocumentMatrix(cleanset1)
tdm1
tdm1 <- as.matrix(tdm1)
tdm1[1:10, 1:20]



# Sentiment analysis

#install the respective packages into Rstudio(uncomment is not installed)
#install.packages("syuzhet") 
#install.packages("lubridate")
#install.packages("ggplot2")
#install.packages("scales")
#install.packages("reshape2")
#install.packages("dplyr")

library(syuzhet)
library(lubridate)
library(ggplot2)
library(scales)
library(reshape2)
library(dplyr)

# Reading file
election <- read.csv(file.choose(), header = T)
mytweet <- iconv(election$text, to = 'utf-8')
election1 <- read.csv(file.choose(), header = T)
mytweet1 <- iconv(election1$text, to = 'utf-8')


# Obtain sentiment scores
s <- get_nrc_sentiment(mytweet)
s1 <- get_nrc_sentiment(mytweet1)
head(s)
head(s1)


# Bar plot
c1<-colSums(s)
c2<-colSums(s1)
sampledata<-data.frame(c1,c2)
barplot(height <- rbind(c1, c2),
        las = 2,
        col = c("blue","red"),
        ylab = 'Count',
        beside = TRUE,
        main = 'Sentiment Scores for Narendra Modi Vs Rahul Gandhi')





