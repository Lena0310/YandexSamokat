SELECT login, count(o.id)
FROM "Couriers" AS c
LEFT JOIN "Orders" AS o ON o."courierId"=c."id" AND "inDelivery" = true
GROUP BY login;