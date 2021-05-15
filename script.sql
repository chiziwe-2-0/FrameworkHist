CREATE TABLE "result" AS
SELECT f.label as framework, level, k."label" as metric, value
	    FROM "values" v
	    join keys k
	    on (v.key_id = k.id)

	   	join metrics m
	   	on (v.id = m.value_id)

	    join frameworks f
	    on (framework_id = f.id)

	    join concurrencies c
	   	on (concurrency_id = c.id);



select * from "result" where framework = 'django' and "level" = 64 and (metric = 'minimum_latency' or metric = 'maximum_latency' or metric = 'average_latency' or metric = 'percentile_50' or metric = 'percentile_75' or metric = 'percentile_90' or metric = 'percentile_99' or metric = 'percentile_99.999') limit 8 offset 16;