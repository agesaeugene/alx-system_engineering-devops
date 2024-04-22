#!/usr/bin/env ruby
#Statistics message transactions  on a TxtMe app

puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
