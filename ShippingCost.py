weight = 41.5

#Ground Shipping
if weight <= 2:
 cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20
elif weight <= 20:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20

print('Ground Shipping Cost: $', cost_ground)

premium_ground = 125

print('Ground shipping premium: $' , premium_ground)

#drone shipping

if weight <= 2:
 cost_drone = weight * 4.5
elif weight <= 6:
  cost_drone = weight * 9
elif weight <= 20:
  cost_drone = weight * 12
else:
  cost_drone = weight * 14.25

print('Drone Shipping Cost: $' , cost_drone)
