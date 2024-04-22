#!/usr/bin/env ruby
# rubby script to accept one argument and pass it to a regular expression matching method

puts ARGV[0].scan(/School/).join
