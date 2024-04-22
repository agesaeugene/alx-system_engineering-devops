#!/usr/bin/env ruby
#Script written in ruby to check for regular expressions written in uppercase

puts ARGV[0].scan(/A-Z]*/).join
