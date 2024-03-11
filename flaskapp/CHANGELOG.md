## [1.8.2](https://github.com/Ebaneck/gorgias-sre-assessment/compare/v1.8.1...v1.8.2) (2024-03-11)


### Bug Fixes

* set exclusively an image tag ([c02ef89](https://github.com/Ebaneck/gorgias-sre-assessment/commit/c02ef89dfa1b7de2ee964d64b281ea89e5c2fb0f))

## [1.8.1](https://github.com/Ebaneck/gorgias-sre-assessment/compare/v1.8.0...v1.8.1) (2024-03-11)


### Bug Fixes

* set default image tag to latest ([8529450](https://github.com/Ebaneck/gorgias-sre-assessment/commit/85294508c897eb62da0c6be400c214a35ee7b74b))

# [1.8.0](https://github.com/Ebaneck/gorgias-sre-assessment/compare/v1.7.0...v1.8.0) (2024-03-11)


### Features

* add readme for helm chart dir ([5d47006](https://github.com/Ebaneck/gorgias-sre-assessment/commit/5d47006bf2498ee0681397d675a894b71f0004c3))

# [1.7.0](https://github.com/Ebaneck/gorgias-sre-assessment/compare/v1.6.0...v1.7.0) (2024-03-11)


### Features

* add & use default pg port ([701111e](https://github.com/Ebaneck/gorgias-sre-assessment/commit/701111ef7d7d9be64c4cbaf9a7c744e29b3fd1b4))
* cleanup dockerfile and app.py ([1b89861](https://github.com/Ebaneck/gorgias-sre-assessment/commit/1b89861df3c95f3ee016110404effecc98e718a6))

# [1.6.0](https://github.com/Ebaneck/gorgias-sre-assessment/compare/v1.5.0...v1.6.0) (2024-03-11)


### Features

* add default for db port ([c01c960](https://github.com/Ebaneck/gorgias-sre-assessment/commit/c01c96023aaae6b27a6409f02a89b8bf85ff4bb6))

# [1.5.0](https://github.com/Ebaneck/gorgias-sre-assessment/compare/v1.4.0...v1.5.0) (2024-03-11)


### Features

* ensure db secret are used ([b6470d6](https://github.com/Ebaneck/gorgias-sre-assessment/commit/b6470d63746effec19abb9955793426830162680))

# [1.4.0](https://github.com/Ebaneck/gorgias-sre-assessment/compare/v1.3.2...v1.4.0) (2024-03-11)


### Features

* add title & description for html template ([4023d6f](https://github.com/Ebaneck/gorgias-sre-assessment/commit/4023d6f535db0729e71acf0a703eae056e3e1211))

## [1.3.2](https://github.com/Ebaneck/gorgias-sre-assessment/compare/v1.3.1...v1.3.2) (2024-03-11)


### Bug Fixes

* add db schema sql file ([940c77f](https://github.com/Ebaneck/gorgias-sre-assessment/commit/940c77f85c2da9fe9e447c9469ce1e088a692fd2))
* donot base64 encode port ([6226150](https://github.com/Ebaneck/gorgias-sre-assessment/commit/622615049ac85e6c3cee4fe104290dfb9575cdc2))

## [1.3.1](https://github.com/Ebaneck/gorgias-sre-assessment/compare/v1.3.0...v1.3.1) (2024-03-11)


### Bug Fixes

* add missing gke deploy envs ([ea57451](https://github.com/Ebaneck/gorgias-sre-assessment/commit/ea5745139a5e8ecbd1fbed95cd976f86c9a86724))
* cleanup app.py ([64177ac](https://github.com/Ebaneck/gorgias-sre-assessment/commit/64177ac15372a19f15b3041b2cc719f650ce93e5))

# [1.3.0](https://github.com/Ebaneck/gorgias-sre-assessment/compare/v1.2.1...v1.3.0) (2024-03-11)


### Features

* add & inject database secrets ([0160659](https://github.com/Ebaneck/gorgias-sre-assessment/commit/01606599619c3dd17642e0467ae0f4ada317ade6))
* add helm values for flask app deployment ([0e4a37c](https://github.com/Ebaneck/gorgias-sre-assessment/commit/0e4a37c95c8634b979956a5852ad09438d2d55e0))
* add helm-charts for flask webapp ([000b5cc](https://github.com/Ebaneck/gorgias-sre-assessment/commit/000b5cc2c97950cb1403e47e89c63f1299b2dad5))
* inject k8s secrets to flask app ([1ff814f](https://github.com/Ebaneck/gorgias-sre-assessment/commit/1ff814f741e2c589f18f86e704fa6f3899edc239))

## [1.2.1](https://github.com/Ebaneck/gorgias-sre-assessment/compare/v1.2.0...v1.2.1) (2024-03-11)


### Bug Fixes

* remove unused html templates ([d1b0487](https://github.com/Ebaneck/gorgias-sre-assessment/commit/d1b04872555de1edd2860a0267916a4da9d7c245))

# [1.2.0](https://github.com/Ebaneck/gorgias-sre-assessment/compare/v1.1.0...v1.2.0) (2024-03-11)


### Features

* add todo app routes ([027a332](https://github.com/Ebaneck/gorgias-sre-assessment/commit/027a332acde4e22b58f5fdfad879b10b2119aae6))

# [1.1.0](https://github.com/Ebaneck/gorgias-sre-assessment/compare/v1.0.0...v1.1.0) (2024-03-11)


### Bug Fixes

* add missing pod labels for pg ([337ecde](https://github.com/Ebaneck/gorgias-sre-assessment/commit/337ecde984988853af8f3ba9d34b14fbc34b5900))


### Features

* add & provision vpc, k8s and node-pools ([9a81656](https://github.com/Ebaneck/gorgias-sre-assessment/commit/9a816560557781d3cf85cd6f8cb1fcb4bb5d6f4e))
* add dedicated node pool for pg ([090d79b](https://github.com/Ebaneck/gorgias-sre-assessment/commit/090d79bee5067fe569ab1e942fe0e925ca36f92e))
* add deployment for pg to gke ([bc27f09](https://github.com/Ebaneck/gorgias-sre-assessment/commit/bc27f0984213087b3294ee46986730413cb09de8))
* add helm values for pg deployment ([234ce47](https://github.com/Ebaneck/gorgias-sre-assessment/commit/234ce47d0ef41a87820ab0beddcb945811c28e48))
* add nginx ingress deployment ([da47dff](https://github.com/Ebaneck/gorgias-sre-assessment/commit/da47dff6d343639a8f5a328f1472fc0fa41eee1c))
* add todo templates from sqlalchemy ([b4ee163](https://github.com/Ebaneck/gorgias-sre-assessment/commit/b4ee1636fd07efe9a54ce8555272f08fe1119c1a))

# 1.0.0 (2024-03-08)


### Features

* add docker-compose file for dev setup ([1829480](https://github.com/Ebaneck/gorgias-sre-assessment/commit/1829480507e5d1ebc707b73d3ffb9e1adf245ef9))
* initial flask application ([9610bd1](https://github.com/Ebaneck/gorgias-sre-assessment/commit/9610bd19545184a2ff7715317cb29b0cec119f45))
