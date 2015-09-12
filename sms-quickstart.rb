require 'rubygems'
require 'twilio-ruby'
require 'sinatra'
require 'pry'

enable :sessions

account_sid = "AC69b643cff49734f97be6c92413bb1431"
auth_token = "ee59c586739b84db680e7e011858a914"
client = Twilio::REST::Client.new account_sid, auth_token

from = "+16304518767" # Your Twilio number

friends = {
"+12243667047" => "Niraj",
"+12246592659" => "Jarin"
}
friends.each do |key, value|
  client.account.messages.create(
    :from => from,
    :to => key,
    :body => "Hey #{value}, Monkey party at 6PM. Bring Bananas!"
  )
  puts "Sent message to #{value}"
end

get '/' do
  "Welcome to rideText"
end

get '/sms-quickstart' do
  session["counter"] ||=0
  sms_count = session["counter"]
  if sms_count == 0
    message = "Welcome! What is your name?"
  else
    message = "Hello, thanks for message number #{sms_count + 1}"
  end
  twiml = Twilio::TwiML::Response.new do |r|
    r.message message
  end
  session["counter"] += 1
  twiml.text
end
