#!/usr/bin/env ruby
# The regular expression repetition [0 - 1]
puts ARGV[0].scan(/hb{0,1}tn/).join
