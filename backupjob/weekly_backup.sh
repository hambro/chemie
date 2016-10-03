#! /bin/bash
cd /code/
if [ "$BACKUP" == "True" ]
then
    NOW=$(date +\%W)
    mkdir /tmp/backup/$NOW -p
    cd /tmp/backup
    zip -r $NOW/media.zip /code/media/
    /usr/bin/pg_dump $POSTGRES_USER -h database > $NOW/backup.sql 2>> /var/log/syslog
    scp -r -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -i /etc/ssl/private/backup/chemiebackup $NOW $BACKUPUSER@$BACKUPHOST:/home/chemiebackup/weekly
    rm -r $NOW
    echo "$(date +'%m.%d.%Y') Weekly backup succeded" >> /var/log/backup.log
else
    echo "$(date +'%m.%d.%Y') No backup for this week" >> /var/log/backup.log
fi

