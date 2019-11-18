#!/usr/bin/env ruby
txt = ARGV
puts txt[0].scan(/^\d{10}$/).join
