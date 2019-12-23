package main

import (
	"flag"
	"fmt"
	"log"
	"os"

	"github.com/coreos/pkg/flagutil"
	"github.com/dghubble/go-twitter/twitter"
	"github.com/dghubble/oauth1"
)

func main() {

	var handle string
	fmt.Printf("Enter the twitter handle:")
	fmt.Scan(&handle)

	flags := flag.NewFlagSet("user-auth", flag.ExitOnError)
	consumerKey := flags.String("consumer-key", "gzc0SiDSqrRcz1f8mVQnpiVTA", "Twitter Consumer Key")
	consumerSecret := flags.String("consumer-secret", "dkqfwwPiNRjEsMRXwT4qsthwuQbGUOCJYnOnsJhjbKDcki63Ck", "Twitter Consumer Secret")
	accessToken := flags.String("access-token", "1168896199006609416-Pj3IwL82BVvMLs7MQMI8QihMYI9CwH", "Twitter Access Token")
	accessSecret := flags.String("access-secret", "AP4EL2CCa1nc7DBGMhxFYz5AP2QKAhoWw58KlAGxiAoOa", "Twitter Access Secret")
	flags.Parse(os.Args[1:])
	flagutil.SetFlagsFromEnv(flags, "TWITTER")

	if *consumerKey == "" || *consumerSecret == "" || *accessToken == "" || *accessSecret == "" {
		log.Fatal("Consumer key/secret and Access token/secret required")
	}

	config := oauth1.NewConfig(*consumerKey, *consumerSecret)
	token := oauth1.NewToken(*accessToken, *accessSecret)
	k := flag.String("twitterHandle", handle, "twitter handle of a user")
	httpClient := config.Client(oauth1.NoContext, token) //requesting for access
	client := twitter.NewClient(httpClient)              //Twitter Client
	f, err := os.Create("Followers.txt")

	params := &twitter.FollowerListParams{
		ScreenName: *k,
	}

	followers, resp, err := client.Followers.List(params)
	var count int = 0
	fmt.Println(resp, err)
	f.WriteString("Some of the followers of " + *k) //this will create a text file starting with "Some of the followers of <username>

	for _, follower := range followers.Users {
		count++
		f.WriteString("\n" + follower.ScreenName) //Writes each follower username to the text file
	}
	f.WriteString("\n")

	f.WriteString(fmt.Sprintf("%d\n", count)) //Writes the counted number of followers in the loop to the text file at the end.

	f.Close()
}
