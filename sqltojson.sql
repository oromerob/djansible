SELECT h.name AS host,vg.name AS config,GROUP_CONCAT('\'',vn.name,'\': \'',vv.value,'\' ') AS json FROM var_value AS vv INNER JOIN var_key AS vk ON vk.id=vv.var_key INNER JOIN host AS h on h.id=vk.host_id INNER JOIN var_group AS vg ON vg.id=vk.var_group_id INNER JOIN var_name AS vn ON vn.id=vv.var_name_id GROUP BY vk.id
