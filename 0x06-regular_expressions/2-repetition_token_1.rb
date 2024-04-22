#!/usr/bin/env ruby
# Script in rubby that accepts one argument and pass it to a regular expression

puts ARGV[0].scan(/hb?t?n/).join
