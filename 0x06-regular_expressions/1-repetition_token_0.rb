#!/usr/bin/env ruby
# The regular expression repetition [2 - 5]
puts ARGV[0].scan(/hbt{2,5}n/).join
