# minecraft-scripts
Scripts for minecraft server automation

## minecraft Server
So you want a quick and simple way to create your own minecraft server?

This repo has Cloudformation Templates (CFTs) that can be used with Amazon Web Services to automatiicaly provision a minecraft server with little effort.

## Instructions

Follow this step by step guide to set up your own minecraft server

### New to AWS?

Create an account

### Log into AWS

### Go to Cloudformation

### Do things

### Server Sizes

The following are AWS sized servers I recommend using for the server. They are included as a paramter in the CFT which default to the smallest.
minecraft runs the entire game on one thread, so none of the crazy multi core CPUs will help the game run any faster.

* t3.micro (REAL SLOW)
* c5.large (BIIIIG)
* z1d.large (STUPID FAST)