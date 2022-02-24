#!/usr/bin/env ruby
# The regular expression repetition [0 - ...]
puts ARGV[0].scan(/hbt{0,}n/).join
