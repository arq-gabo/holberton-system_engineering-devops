#!/usr/bin/env ruby
txt = ARGV
puts txt[0].scan(/from:(.+|\d)\].*to:(\+?\d+).*flags:(-?\d:-?\d:-?\d:-?\d:-?\d)/).join(',')
