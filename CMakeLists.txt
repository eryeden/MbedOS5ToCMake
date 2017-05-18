cmake_minimum_required(VERSION 3.8)
project(test1 C CXX ASM)

#SET(CMAKE_VERBOSE_MAKEFILE ON)


#set(CMAKE_CXX_STANDARD 11)

#INCLUDE(CMakeForceCompiler)

#SET(CMAKE_SYSTEM_NAME Generic)
SET(CMAKE_SYSTEM_VERSION 1)

#Timestamp
string(TIMESTAMP TIMESTAMP_TEST %Y%m%d%H%M%S UTC)
message(${TIMESTAMP_TEST})

#CMAKE_CONFIGURATION_TYPES
SET(CMAKE_CONFIGURATION_TYPES Debug Release)

SET(TOOLCHAIN_DIR /opt/env/gcc-arm-none-eabi-5_4-2016q3/bin)


#settings
######################################
SET(SRCS ${PROJECT_SOURCE_DIR}/main.cpp ${PROJECT_SOURCE_DIR}/mbed-os/drivers/AnalogIn.cpp ${PROJECT_SOURCE_DIR}/mbed-os/drivers/BusIn.cpp ${PROJECT_SOURCE_DIR}/mbed-os/drivers/BusInOut.cpp ${PROJECT_SOURCE_DIR}/mbed-os/drivers/BusOut.cpp ${PROJECT_SOURCE_DIR}/mbed-os/drivers/CAN.cpp ${PROJECT_SOURCE_DIR}/mbed-os/drivers/Ethernet.cpp ${PROJECT_SOURCE_DIR}/mbed-os/drivers/FileBase.cpp ${PROJECT_SOURCE_DIR}/mbed-os/drivers/FilePath.cpp ${PROJECT_SOURCE_DIR}/mbed-os/drivers/FileSystemLike.cpp ${PROJECT_SOURCE_DIR}/mbed-os/drivers/FlashIAP.cpp ${PROJECT_SOURCE_DIR}/mbed-os/drivers/I2C.cpp ${PROJECT_SOURCE_DIR}/mbed-os/drivers/I2CSlave.cpp ${PROJECT_SOURCE_DIR}/mbed-os/drivers/InterruptIn.cpp ${PROJECT_SOURCE_DIR}/mbed-os/drivers/InterruptManager.cpp ${PROJECT_SOURCE_DIR}/mbed-os/drivers/LocalFileSystem.cpp ${PROJECT_SOURCE_DIR}/mbed-os/drivers/RawSerial.cpp ${PROJECT_SOURCE_DIR}/mbed-os/drivers/SPI.cpp ${PROJECT_SOURCE_DIR}/mbed-os/drivers/SPISlave.cpp ${PROJECT_SOURCE_DIR}/mbed-os/drivers/Serial.cpp ${PROJECT_SOURCE_DIR}/mbed-os/drivers/SerialBase.cpp ${PROJECT_SOURCE_DIR}/mbed-os/drivers/Stream.cpp ${PROJECT_SOURCE_DIR}/mbed-os/drivers/Ticker.cpp ${PROJECT_SOURCE_DIR}/mbed-os/drivers/Timeout.cpp ${PROJECT_SOURCE_DIR}/mbed-os/drivers/Timer.cpp ${PROJECT_SOURCE_DIR}/mbed-os/drivers/TimerEvent.cpp ${PROJECT_SOURCE_DIR}/mbed-os/events/EventQueue.cpp ${PROJECT_SOURCE_DIR}/mbed-os/events/equeue/equeue.c ${PROJECT_SOURCE_DIR}/mbed-os/events/equeue/equeue_mbed.cpp ${PROJECT_SOURCE_DIR}/mbed-os/events/equeue/equeue_posix.c ${PROJECT_SOURCE_DIR}/mbed-os/features/filesystem/Dir.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/filesystem/File.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/filesystem/FileSystem.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/filesystem/bd/ChainingBlockDevice.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/filesystem/bd/HeapBlockDevice.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/filesystem/bd/SlicingBlockDevice.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/filesystem/fat/ChaN/ccsbcs.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/filesystem/fat/ChaN/ff.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/filesystem/fat/FATFileSystem.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/frameworks/greentea-client/source/greentea_metrics.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/frameworks/greentea-client/source/greentea_serial.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/frameworks/greentea-client/source/greentea_test_env.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/frameworks/unity/source/unity.c ${PROJECT_SOURCE_DIR}/mbed-os/features/frameworks/utest/mbed-utest-shim.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/frameworks/utest/source/unity_handler.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/frameworks/utest/source/utest_case.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/frameworks/utest/source/utest_default_handlers.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/frameworks/utest/source/utest_greentea_handlers.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/frameworks/utest/source/utest_harness.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/frameworks/utest/source/utest_shim.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/frameworks/utest/source/utest_stack_trace.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/frameworks/utest/source/utest_types.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/platform/src/mbed_trng.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/aes.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/aesni.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/arc4.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/asn1parse.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/asn1write.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/base64.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/bignum.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/blowfish.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/camellia.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/ccm.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/certs.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/cipher.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/cipher_wrap.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/cmac.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/ctr_drbg.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/debug.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/des.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/dhm.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/ecdh.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/ecdsa.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/ecjpake.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/ecp.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/ecp_curves.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/entropy.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/entropy_poll.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/error.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/gcm.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/havege.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/hmac_drbg.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/md.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/md2.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/md4.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/md5.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/md_wrap.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/memory_buffer_alloc.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/net_sockets.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/oid.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/padlock.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/pem.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/pk.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/pk_wrap.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/pkcs11.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/pkcs12.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/pkcs5.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/pkparse.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/pkwrite.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/platform.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/ripemd160.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/rsa.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/sha1.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/sha256.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/sha512.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/ssl_cache.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/ssl_ciphersuites.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/ssl_cli.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/ssl_cookie.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/ssl_srv.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/ssl_ticket.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/ssl_tls.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/threading.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/timing.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/version.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/version_features.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/x509.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/x509_create.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/x509_crl.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/x509_crt.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/x509_csr.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/x509write_crt.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/x509write_csr.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src/xtea.c ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/targets/TARGET_STM/aes_alt.c ${PROJECT_SOURCE_DIR}/mbed-os/features/netsocket/NetworkInterface.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/netsocket/NetworkStack.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/netsocket/Socket.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/netsocket/SocketAddress.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/netsocket/TCPServer.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/netsocket/TCPSocket.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/netsocket/UDPSocket.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/netsocket/WiFiAccessPoint.cpp ${PROJECT_SOURCE_DIR}/mbed-os/features/netsocket/nsapi_dns.cpp ${PROJECT_SOURCE_DIR}/mbed-os/hal/mbed_gpio.c ${PROJECT_SOURCE_DIR}/mbed-os/hal/mbed_lp_ticker_api.c ${PROJECT_SOURCE_DIR}/mbed-os/hal/mbed_pinmap_common.c ${PROJECT_SOURCE_DIR}/mbed-os/hal/mbed_ticker_api.c ${PROJECT_SOURCE_DIR}/mbed-os/hal/mbed_us_ticker_api.c ${PROJECT_SOURCE_DIR}/mbed-os/platform/CallChain.cpp ${PROJECT_SOURCE_DIR}/mbed-os/platform/mbed_alloc_wrappers.cpp ${PROJECT_SOURCE_DIR}/mbed-os/platform/mbed_application.c ${PROJECT_SOURCE_DIR}/mbed-os/platform/mbed_assert.c ${PROJECT_SOURCE_DIR}/mbed-os/platform/mbed_board.c ${PROJECT_SOURCE_DIR}/mbed-os/platform/mbed_critical.c ${PROJECT_SOURCE_DIR}/mbed-os/platform/mbed_error.c ${PROJECT_SOURCE_DIR}/mbed-os/platform/mbed_interface.c ${PROJECT_SOURCE_DIR}/mbed-os/platform/mbed_mem_trace.c ${PROJECT_SOURCE_DIR}/mbed-os/platform/mbed_retarget.cpp ${PROJECT_SOURCE_DIR}/mbed-os/platform/mbed_rtc_time.cpp ${PROJECT_SOURCE_DIR}/mbed-os/platform/mbed_semihost_api.c ${PROJECT_SOURCE_DIR}/mbed-os/platform/mbed_stats.c ${PROJECT_SOURCE_DIR}/mbed-os/platform/mbed_wait_api_no_rtos.c ${PROJECT_SOURCE_DIR}/mbed-os/platform/mbed_wait_api_rtos.cpp ${PROJECT_SOURCE_DIR}/mbed-os/rtos/Mutex.cpp ${PROJECT_SOURCE_DIR}/mbed-os/rtos/RtosTimer.cpp ${PROJECT_SOURCE_DIR}/mbed-os/rtos/Semaphore.cpp ${PROJECT_SOURCE_DIR}/mbed-os/rtos/Thread.cpp ${PROJECT_SOURCE_DIR}/mbed-os/rtos/rtos_idle.c ${PROJECT_SOURCE_DIR}/mbed-os/rtos/rtx/TARGET_CORTEX_M/HAL_CM.c ${PROJECT_SOURCE_DIR}/mbed-os/rtos/rtx/TARGET_CORTEX_M/RTX_Conf_CM.c ${PROJECT_SOURCE_DIR}/mbed-os/rtos/rtx/TARGET_CORTEX_M/TARGET_RTOS_M4_M7/TOOLCHAIN_GCC/HAL_CM4.S ${PROJECT_SOURCE_DIR}/mbed-os/rtos/rtx/TARGET_CORTEX_M/TARGET_RTOS_M4_M7/TOOLCHAIN_GCC/SVC_Table.S ${PROJECT_SOURCE_DIR}/mbed-os/rtos/rtx/TARGET_CORTEX_M/rt_CMSIS.c ${PROJECT_SOURCE_DIR}/mbed-os/rtos/rtx/TARGET_CORTEX_M/rt_Event.c ${PROJECT_SOURCE_DIR}/mbed-os/rtos/rtx/TARGET_CORTEX_M/rt_List.c ${PROJECT_SOURCE_DIR}/mbed-os/rtos/rtx/TARGET_CORTEX_M/rt_Mailbox.c ${PROJECT_SOURCE_DIR}/mbed-os/rtos/rtx/TARGET_CORTEX_M/rt_MemBox.c ${PROJECT_SOURCE_DIR}/mbed-os/rtos/rtx/TARGET_CORTEX_M/rt_Memory.c ${PROJECT_SOURCE_DIR}/mbed-os/rtos/rtx/TARGET_CORTEX_M/rt_Mutex.c ${PROJECT_SOURCE_DIR}/mbed-os/rtos/rtx/TARGET_CORTEX_M/rt_OsEventObserver.c ${PROJECT_SOURCE_DIR}/mbed-os/rtos/rtx/TARGET_CORTEX_M/rt_Robin.c ${PROJECT_SOURCE_DIR}/mbed-os/rtos/rtx/TARGET_CORTEX_M/rt_Semaphore.c ${PROJECT_SOURCE_DIR}/mbed-os/rtos/rtx/TARGET_CORTEX_M/rt_System.c ${PROJECT_SOURCE_DIR}/mbed-os/rtos/rtx/TARGET_CORTEX_M/rt_Task.c ${PROJECT_SOURCE_DIR}/mbed-os/rtos/rtx/TARGET_CORTEX_M/rt_Time.c ${PROJECT_SOURCE_DIR}/mbed-os/rtos/rtx/TARGET_CORTEX_M/rt_Timer.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/TARGET_STM32L432xC/TARGET_NUCLEO_L432KC/PeripheralPins.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/TARGET_STM32L432xC/TARGET_NUCLEO_L432KC/system_stm32l4xx.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/TARGET_STM32L432xC/device/TOOLCHAIN_GCC_ARM/startup_stm32l432xx.S ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/TARGET_STM32L432xC/device/cmsis_nvic.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/analogin_api.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/analogout_api.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_adc.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_adc_ex.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_can.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_comp.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_cortex.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_crc.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_crc_ex.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_cryp.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_cryp_ex.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_dac.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_dac_ex.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_dfsdm.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_dma.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_firewall.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_flash.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_flash_ex.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_flash_ramfunc.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_gpio.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_hcd.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_i2c.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_i2c_ex.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_irda.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_iwdg.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_lcd.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_lptim.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_msp_template.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_nand.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_nor.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_opamp.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_opamp_ex.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_pcd.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_pcd_ex.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_pwr.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_pwr_ex.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_qspi.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_rcc.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_rcc_ex.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_rng.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_rtc.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_rtc_ex.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_sai.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_sd.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_smartcard.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_smartcard_ex.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_smbus.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_spi.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_spi_ex.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_sram.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_swpmi.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_tim.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_tim_ex.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_tsc.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_uart.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_uart_ex.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_usart.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_hal_wwdg.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_ll_adc.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_ll_comp.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_ll_crc.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_ll_crs.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_ll_dac.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_ll_dma.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_ll_exti.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_ll_fmc.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_ll_gpio.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_ll_i2c.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_ll_lptim.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_ll_lpuart.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_ll_opamp.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_ll_pwr.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_ll_rcc.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_ll_rng.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_ll_rtc.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_ll_sdmmc.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_ll_spi.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_ll_swpmi.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_ll_tim.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_ll_usart.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_ll_usb.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device/stm32l4xx_ll_utils.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/gpio_irq_device.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/mbed_overrides.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/pwmout_device.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/serial_api.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/spi_api.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/can_api.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/gpio_api.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/gpio_irq_api.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/hal_tick_16b.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/hal_tick_32b.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/i2c_api.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/lp_ticker.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/pinmap.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/port_api.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/pwmout_api.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/rtc_api.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/sleep.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/stm_spi_api.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/trng_api.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/us_ticker_16b.c ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/us_ticker_32b.c)
######################################
SET(INCDIR ${PROJECT_SOURCE_DIR} ${PROJECT_SOURCE_DIR}/img ${PROJECT_SOURCE_DIR}/mbed-os ${PROJECT_SOURCE_DIR}/mbed-os/cmsis ${PROJECT_SOURCE_DIR}/mbed-os/cmsis/TOOLCHAIN_GCC ${PROJECT_SOURCE_DIR}/mbed-os/drivers ${PROJECT_SOURCE_DIR}/mbed-os/events ${PROJECT_SOURCE_DIR}/mbed-os/events/equeue ${PROJECT_SOURCE_DIR}/mbed-os/features ${PROJECT_SOURCE_DIR}/mbed-os/features/filesystem ${PROJECT_SOURCE_DIR}/mbed-os/features/filesystem/bd ${PROJECT_SOURCE_DIR}/mbed-os/features/filesystem/fat ${PROJECT_SOURCE_DIR}/mbed-os/features/filesystem/fat/ChaN ${PROJECT_SOURCE_DIR}/mbed-os/features/frameworks ${PROJECT_SOURCE_DIR}/mbed-os/features/frameworks/greentea-client ${PROJECT_SOURCE_DIR}/mbed-os/features/frameworks/greentea-client/greentea-client ${PROJECT_SOURCE_DIR}/mbed-os/features/frameworks/greentea-client/source ${PROJECT_SOURCE_DIR}/mbed-os/features/frameworks/unity ${PROJECT_SOURCE_DIR}/mbed-os/features/frameworks/unity/source ${PROJECT_SOURCE_DIR}/mbed-os/features/frameworks/unity/unity ${PROJECT_SOURCE_DIR}/mbed-os/features/frameworks/utest ${PROJECT_SOURCE_DIR}/mbed-os/features/frameworks/utest/source ${PROJECT_SOURCE_DIR}/mbed-os/features/frameworks/utest/utest ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/importer ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/inc ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/inc/mbedtls ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/platform ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/platform/inc ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/platform/src ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/src ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/targets ${PROJECT_SOURCE_DIR}/mbed-os/features/mbedtls/targets/TARGET_STM ${PROJECT_SOURCE_DIR}/mbed-os/features/nanostack ${PROJECT_SOURCE_DIR}/mbed-os/features/netsocket ${PROJECT_SOURCE_DIR}/mbed-os/features/storage ${PROJECT_SOURCE_DIR}/mbed-os/hal ${PROJECT_SOURCE_DIR}/mbed-os/hal/storage_abstraction ${PROJECT_SOURCE_DIR}/mbed-os/platform ${PROJECT_SOURCE_DIR}/mbed-os/rtos ${PROJECT_SOURCE_DIR}/mbed-os/rtos/rtx ${PROJECT_SOURCE_DIR}/mbed-os/rtos/rtx/TARGET_CORTEX_M ${PROJECT_SOURCE_DIR}/mbed-os/rtos/rtx/TARGET_CORTEX_M/TARGET_RTOS_M4_M7 ${PROJECT_SOURCE_DIR}/mbed-os/rtos/rtx/TARGET_CORTEX_M/TARGET_RTOS_M4_M7/TOOLCHAIN_GCC ${PROJECT_SOURCE_DIR}/mbed-os/targets ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4 ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/TARGET_STM32L432xC ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/TARGET_STM32L432xC/TARGET_NUCLEO_L432KC ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/TARGET_STM32L432xC/device ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/TARGET_STM32L432xC/device/TOOLCHAIN_GCC_ARM ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/device)

######################################
#SET(CFLGS " -std=gnu99 -DDEVICE_SPI=1 -D__MBED__=1 -DDEVICE_I2CSLAVE=1 -DTARGET_LIKE_MBED -DDEVICE_PORTOUT=1 -DDEVICE_PORTINOUT=1 -DTARGET_RTOS_M4_M7 -DMBED_BUILD_TIMESTAMP=1495020646.98 -DDEVICE_RTC=1 -DTOOLCHAIN_object -D__CMSIS_RTOS -DTOOLCHAIN_GCC -DDEVICE_I2C_ASYNCH=1 -DTARGET_CORTEX_M -DTARGET_DEBUG -DTARGET_LIKE_CORTEX_M4 -DDEVICE_ANALOGOUT=1 -DTARGET_M4 -DTARGET_UVISOR_UNSUPPORTED -DTARGET_STM32L4 -DDEVICE_SPI_ASYNCH=1 -DDEVICE_SERIAL=1 -DTARGET_STM32L432xC -DDEVICE_I2C=1 -DTRANSACTION_QUEUE_SIZE_SPI=2 -D__CORTEX_M4 -DDEVICE_STDIO_MESSAGES=1 -D__FPU_PRESENT=1 -DDEVICE_LOWPOWERTIMER=1 -DTARGET_FF_ARDUINO -DDEVICE_PORTIN=1 -DTARGET_STM -DTARGET_STM32L432KC -DDEVICE_SERIAL_FC=1 -DDEVICE_TRNG=1 -D__MBED_CMSIS_RTOS_CM -DDEVICE_SLEEP=1 -DTOOLCHAIN_GCC_ARM -DDEVICE_CAN=1 -DDEVICE_INTERRUPTIN=1 -DDEVICE_SPISLAVE=1 -DDEVICE_ANALOGIN=1 -DDEVICE_PWMOUT=1 -DTARGET_NUCLEO_L432KC -DARM_MATH_CM4 -include ${PROJECT_SOURCE_DIR}/mbed_config.h")

SET(CFLGS_DEBUG " -std=gnu99 -DDEVICE_SPI=1 -D__MBED__=1 -DDEVICE_I2CSLAVE=1 -DTARGET_LIKE_MBED -DDEVICE_PORTOUT=1 -DDEVICE_PORTINOUT=1 -DTARGET_RTOS_M4_M7 -DDEVICE_LOWPOWERTIMER=1 -DDEVICE_RTC=1 -DTOOLCHAIN_object -D__CMSIS_RTOS -DMBED_BUILD_TIMESTAMP=${TIMESTAMP_TEST} -DTOOLCHAIN_GCC -DDEVICE_I2C_ASYNCH=1 -DTARGET_CORTEX_M -DTARGET_DEBUG -DTARGET_LIKE_CORTEX_M4 -DDEVICE_ANALOGOUT=1 -DTARGET_M4 -DTARGET_UVISOR_UNSUPPORTED -DTARGET_STM32L4 -DDEVICE_SPI_ASYNCH=1 -DDEVICE_SERIAL=1 -DTARGET_STM32L432xC -DDEVICE_I2C=1 -DTRANSACTION_QUEUE_SIZE_SPI=2 -D__CORTEX_M4 -DDEVICE_STDIO_MESSAGES=1 -D__FPU_PRESENT=1 -DTARGET_FF_ARDUINO -DDEVICE_PORTIN=1 -DTARGET_STM -DTARGET_STM32L432KC -DDEVICE_SERIAL_FC=1 -DDEVICE_TRNG=1 -D__MBED_CMSIS_RTOS_CM -DDEVICE_SLEEP=1 -DTOOLCHAIN_GCC_ARM -DDEVICE_CAN=1 -DDEVICE_INTERRUPTIN=1 -DDEVICE_SPISLAVE=1 -DDEVICE_ANALOGIN=1 -DDEVICE_PWMOUT=1 -DTARGET_NUCLEO_L432KC -DARM_MATH_CM4 -include ${PROJECT_SOURCE_DIR}/mbed_config.h")

SET(CFLGS_RELEASE " -std=gnu99 -DDEVICE_SPI=1 -D__MBED__=1 -DDEVICE_I2CSLAVE=1 -DTARGET_LIKE_MBED -DDEVICE_PORTOUT=1 -DDEVICE_PORTINOUT=1 -DTARGET_RTOS_M4_M7 -DMBED_BUILD_TIMESTAMP=${TIMESTAMP_TEST} -DDEVICE_RTC=1 -DTOOLCHAIN_object -D__CMSIS_RTOS -DTOOLCHAIN_GCC -DDEVICE_I2C_ASYNCH=1 -DTARGET_CORTEX_M -DTARGET_DEBUG -DTARGET_LIKE_CORTEX_M4 -DDEVICE_ANALOGOUT=1 -DTARGET_M4 -DTARGET_UVISOR_UNSUPPORTED -DTARGET_STM32L4 -DDEVICE_SPI_ASYNCH=1 -DDEVICE_SERIAL=1 -DTARGET_STM32L432xC -DDEVICE_I2C=1 -DTRANSACTION_QUEUE_SIZE_SPI=2 -D__CORTEX_M4 -DDEVICE_STDIO_MESSAGES=1 -D__FPU_PRESENT=1 -DDEVICE_LOWPOWERTIMER=1 -DTARGET_FF_ARDUINO -DDEVICE_PORTIN=1 -DTARGET_STM -DTARGET_STM32L432KC -DDEVICE_SERIAL_FC=1 -DDEVICE_TRNG=1 -D__MBED_CMSIS_RTOS_CM -DDEVICE_SLEEP=1 -DTOOLCHAIN_GCC_ARM -DDEVICE_CAN=1 -DDEVICE_INTERRUPTIN=1 -DDEVICE_SPISLAVE=1 -DDEVICE_ANALOGIN=1 -DDEVICE_PWMOUT=1 -DTARGET_NUCLEO_L432KC -DARM_MATH_CM4 -include ${PROJECT_SOURCE_DIR}/mbed_config.h")

SET(CFLGS ${CFLAGS_RELEASE})


######################################
#SET(CXXFLGS " -std=gnu++98 -fno-rtti -Wvla -DDEVICE_SPI=1 -D__MBED__=1 -DDEVICE_I2CSLAVE=1 -DTARGET_LIKE_MBED -DDEVICE_PORTOUT=1 -DDEVICE_PORTINOUT=1 -DTARGET_RTOS_M4_M7 -DMBED_BUILD_TIMESTAMP=1495020646.98 -DDEVICE_RTC=1 -DTOOLCHAIN_object -D__CMSIS_RTOS -DTOOLCHAIN_GCC -DDEVICE_I2C_ASYNCH=1 -DTARGET_CORTEX_M -DTARGET_DEBUG -DTARGET_LIKE_CORTEX_M4 -DDEVICE_ANALOGOUT=1 -DTARGET_M4 -DTARGET_UVISOR_UNSUPPORTED -DTARGET_STM32L4 -DDEVICE_SPI_ASYNCH=1 -DDEVICE_SERIAL=1 -DTARGET_STM32L432xC -DDEVICE_I2C=1 -DTRANSACTION_QUEUE_SIZE_SPI=2 -D__CORTEX_M4 -DDEVICE_STDIO_MESSAGES=1 -D__FPU_PRESENT=1 -DDEVICE_LOWPOWERTIMER=1 -DTARGET_FF_ARDUINO -DDEVICE_PORTIN=1 -DTARGET_STM -DTARGET_STM32L432KC -DDEVICE_SERIAL_FC=1 -DDEVICE_TRNG=1 -D__MBED_CMSIS_RTOS_CM -DDEVICE_SLEEP=1 -DTOOLCHAIN_GCC_ARM -DDEVICE_CAN=1 -DDEVICE_INTERRUPTIN=1 -DDEVICE_SPISLAVE=1 -DDEVICE_ANALOGIN=1 -DDEVICE_PWMOUT=1 -DTARGET_NUCLEO_L432KC -DARM_MATH_CM4 -include ${PROJECT_SOURCE_DIR}/mbed_config.h")

SET(CXXFLGS_DEBUG " -std=gnu++98 -fno-rtti -Wvla -DDEVICE_SPI=1 -D__MBED__=1 -DDEVICE_I2CSLAVE=1 -DTARGET_LIKE_MBED -DDEVICE_PORTOUT=1 -DDEVICE_PORTINOUT=1 -DTARGET_RTOS_M4_M7 -DDEVICE_LOWPOWERTIMER=1 -DDEVICE_RTC=1 -DTOOLCHAIN_object -D__CMSIS_RTOS -DMBED_BUILD_TIMESTAMP=${TIMESTAMP_TEST} -DTOOLCHAIN_GCC -DDEVICE_I2C_ASYNCH=1 -DTARGET_CORTEX_M -DTARGET_DEBUG -DTARGET_LIKE_CORTEX_M4 -DDEVICE_ANALOGOUT=1 -DTARGET_M4 -DTARGET_UVISOR_UNSUPPORTED -DTARGET_STM32L4 -DDEVICE_SPI_ASYNCH=1 -DDEVICE_SERIAL=1 -DTARGET_STM32L432xC -DDEVICE_I2C=1 -DTRANSACTION_QUEUE_SIZE_SPI=2 -D__CORTEX_M4 -DDEVICE_STDIO_MESSAGES=1 -D__FPU_PRESENT=1 -DTARGET_FF_ARDUINO -DDEVICE_PORTIN=1 -DTARGET_STM -DTARGET_STM32L432KC -DDEVICE_SERIAL_FC=1 -DDEVICE_TRNG=1 -D__MBED_CMSIS_RTOS_CM -DDEVICE_SLEEP=1 -DTOOLCHAIN_GCC_ARM -DDEVICE_CAN=1 -DDEVICE_INTERRUPTIN=1 -DDEVICE_SPISLAVE=1 -DDEVICE_ANALOGIN=1 -DDEVICE_PWMOUT=1 -DTARGET_NUCLEO_L432KC -DARM_MATH_CM4 -include ${PROJECT_SOURCE_DIR}/mbed_config.h")

SET(CXXFLGS_RELEASE " -std=gnu++98 -fno-rtti -Wvla -DDEVICE_SPI=1 -D__MBED__=1 -DDEVICE_I2CSLAVE=1 -DTARGET_LIKE_MBED -DDEVICE_PORTOUT=1 -DDEVICE_PORTINOUT=1 -DTARGET_RTOS_M4_M7 -DMBED_BUILD_TIMESTAMP=${TIMESTAMP_TEST} -DDEVICE_RTC=1 -DTOOLCHAIN_object -D__CMSIS_RTOS -DTOOLCHAIN_GCC -DDEVICE_I2C_ASYNCH=1 -DTARGET_CORTEX_M -DTARGET_DEBUG -DTARGET_LIKE_CORTEX_M4 -DDEVICE_ANALOGOUT=1 -DTARGET_M4 -DTARGET_UVISOR_UNSUPPORTED -DTARGET_STM32L4 -DDEVICE_SPI_ASYNCH=1 -DDEVICE_SERIAL=1 -DTARGET_STM32L432xC -DDEVICE_I2C=1 -DTRANSACTION_QUEUE_SIZE_SPI=2 -D__CORTEX_M4 -DDEVICE_STDIO_MESSAGES=1 -D__FPU_PRESENT=1 -DDEVICE_LOWPOWERTIMER=1 -DTARGET_FF_ARDUINO -DDEVICE_PORTIN=1 -DTARGET_STM -DTARGET_STM32L432KC -DDEVICE_SERIAL_FC=1 -DDEVICE_TRNG=1 -D__MBED_CMSIS_RTOS_CM -DDEVICE_SLEEP=1 -DTOOLCHAIN_GCC_ARM -DDEVICE_CAN=1 -DDEVICE_INTERRUPTIN=1 -DDEVICE_SPISLAVE=1 -DDEVICE_ANALOGIN=1 -DDEVICE_PWMOUT=1 -DTARGET_NUCLEO_L432KC -DARM_MATH_CM4 -include ${PROJECT_SOURCE_DIR}/mbed_config.h")

SET(CXXFLGS ${CXXFLGS_RELEASE})


######################################
#SET(ASMFLGS " -x assembler-with-cpp -DTRANSACTION_QUEUE_SIZE_SPI=2 -D__CORTEX_M4 -DARM_MATH_CM4 -D__FPU_PRESENT=1 -D__MBED_CMSIS_RTOS_CM -D__CMSIS_RTOS")
SET(ASMFLGS_DEBUG " -x assembler-with-cpp -DTRANSACTION_QUEUE_SIZE_SPI=2 -D__CORTEX_M4 -DARM_MATH_CM4 -D__FPU_PRESENT=1 -D__MBED_CMSIS_RTOS_CM -D__CMSIS_RTOS")
SET(ASMFLGS_RELEASE " -x assembler-with-cpp -DTRANSACTION_QUEUE_SIZE_SPI=2 -D__CORTEX_M4 -DARM_MATH_CM4 -D__FPU_PRESENT=1 -D__MBED_CMSIS_RTOS_CM -D__CMSIS_RTOS")
SET(ASMFLGS ${ASMFLGS_RELEASE})



# SET(CMP_COMMON_CMD "-c -Wall -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -fmessage-length=0 -fno-exceptions -fno-builtin -ffunction-sections -fdata-sections -funsigned-char -MMD -fno-delete-null-pointer-checks -fomit-frame-pointer -O0 -g3")

# SET(ASM_CMD "-x assembler-with-cpp ${CMP_COMMON_CMD}")
# SET(C_CMD "-std=gnu99 ${CMP_COMMON_CMD}")
# SET(CXX_CMD "-std=gnu++98 -fno-rtti -Wvla ${CMP_COMMON_CMD}")







# ######################################
# SET(ASM_CMD " -x assembler-with-cpp -c -Wall -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -fmessage-length=0 -fno-exceptions -fno-builtin -ffunction-sections -fdata-sections -funsigned-char -MMD -fno-delete-null-pointer-checks -fomit-frame-pointer -O0 -g3 -mcpu=cortex-m4 -mthumb -mfpu=fpv4-sp-d16 -mfloat-abi=softfp ")
# #SET(ASM_CMD " -g3 -gdwarf-3 -x assembler-with-cpp -c -Wall -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -fmessage-length=0 -fno-exceptions -fno-builtin -ffunction-sections -fdata-sections -funsigned-char -MMD -fno-delete-null-pointer-checks -fomit-frame-pointer -mcpu=cortex-m4 -mthumb -mfpu=fpv4-sp-d16 -mfloat-abi=softfp")
SET(ASM_CMD_RELEASE " -x assembler-with-cpp -c -Wall -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -fmessage-length=0 -fno-exceptions -fno-builtin -ffunction-sections -fdata-sections -funsigned-char -MMD -fno-delete-null-pointer-checks -fomit-frame-pointer -O3 -mcpu=cortex-m4 -mthumb -mfpu=fpv4-sp-d16 -mfloat-abi=softfp ")
SET(ASM_CMD_DEBUG " -x assembler-with-cpp -c -Wall -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -fmessage-length=0 -fno-exceptions -fno-builtin -ffunction-sections -fdata-sections -funsigned-char -MMD -fno-delete-null-pointer-checks -fomit-frame-pointer -O0 -g3 -mcpu=cortex-m4 -mthumb -mfpu=fpv4-sp-d16 -mfloat-abi=softfp ")
SET(ASM_CMD ${ASM_CMD_RELEASE})


# ######################################
# SET(C_CMD " -std=gnu99 -c -Wall -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -fmessage-length=0 -fno-exceptions -fno-builtin -ffunction-sections -fdata-sections -funsigned-char -MMD -fno-delete-null-pointer-checks -fomit-frame-pointer -O0 -g3 -mcpu=cortex-m4 -mthumb -mfpu=fpv4-sp-d16 -mfloat-abi=softfp ")
# #SET(C_CMD " -g3 -gdwarf-3 -std=gnu99 -c -Wall -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -fmessage-length=0 -fno-exceptions -fno-builtin -ffunction-sections -fdata-sections -funsigned-char -MMD -fno-delete-null-pointer-checks -fomit-frame-pointer -mcpu=cortex-m4 -mthumb -mfpu=fpv4-sp-d16 -mfloat-abi=softfp")

SET(C_CMD_DEBUG " -std=gnu99 -c -Wall -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -fmessage-length=0 -fno-exceptions -fno-builtin -ffunction-sections -fdata-sections -funsigned-char -MMD -fno-delete-null-pointer-checks -fomit-frame-pointer -O0 -g3 -mcpu=cortex-m4 -mthumb -mfpu=fpv4-sp-d16 -mfloat-abi=softfp ")
SET(C_CMD_RELEASE " -std=gnu99 -c -Wall -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -fmessage-length=0 -fno-exceptions -fno-builtin -ffunction-sections -fdata-sections -funsigned-char -MMD -fno-delete-null-pointer-checks -fomit-frame-pointer -O3 -mcpu=cortex-m4 -mthumb -mfpu=fpv4-sp-d16 -mfloat-abi=softfp ")
SET(C_CMD ${C_CMD_RELEASE})


# ######################################
# SET(CXX_CMD " -std=gnu++98 -fno-rtti -Wvla -c -Wall -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -fmessage-length=0 -fno-exceptions -fno-builtin -ffunction-sections -fdata-sections -funsigned-char -MMD -fno-delete-null-pointer-checks -fomit-frame-pointer -O0 -g3 -mcpu=cortex-m4 -mthumb -mfpu=fpv4-sp-d16 -mfloat-abi=softfp ")
# #SET(CXX_CMD " -g3 -gdwarf-3 -std=gnu++98 -fno-rtti -Wvla -c -Wall -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -fmessage-length=0 -fno-exceptions -fno-builtin -ffunction-sections -fdata-sections -funsigned-char -MMD -fno-delete-null-pointer-checks -fomit-frame-pointer -mcpu=cortex-m4 -mthumb -mfpu=fpv4-sp-d16 -mfloat-abi=softfp")

SET(CXX_CMD_DEBUG " -std=gnu++98 -fno-rtti -Wvla -c -Wall -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -fmessage-length=0 -fno-exceptions -fno-builtin -ffunction-sections -fdata-sections -funsigned-char -MMD -fno-delete-null-pointer-checks -fomit-frame-pointer -O0 -g3 -mcpu=cortex-m4 -mthumb -mfpu=fpv4-sp-d16 -mfloat-abi=softfp ")
SET(CXX_CMD_RELEASE " -std=gnu++98 -fno-rtti -Wvla -c -Wall -Wextra -Wno-unused-parameter -Wno-missing-field-initializers -fmessage-length=0 -fno-exceptions -fno-builtin -ffunction-sections -fdata-sections -funsigned-char -MMD -fno-delete-null-pointer-checks -fomit-frame-pointer -O3 -mcpu=cortex-m4 -mthumb -mfpu=fpv4-sp-d16 -mfloat-abi=softfp ")
SET(CXX_CMD ${CXX_CMD_RELEASE})


######################################
# debug
SET(DEBUG_PARAM "-g -gdwarf-3")

# SET(ASM_CMD "${ASM_CMD} ${DEBUG_PARAM}")
# SET(C_CMD "${C_CMD} ${DEBUG_PARAM}")
# SET(CXX_CMD "${CXX_CMD} ${DEBUG_PARAM}")




SET(LD_CMD arm-none-eabi-gcc)

SET(ELF_CMD arm-none-eabi-objcopy )

SET(PREP_CMD "arm-none-eabi-cpp -E -P -Wl,--gc-sections -Wl,--wrap,main -Wl,--wrap,_malloc_r -Wl,--wrap,_free_r -Wl,--wrap,_realloc_r -Wl,--wrap,_calloc_r -Wl,--wrap,exit -Wl,--wrap,atexit -Wl,-n --specs=nano.specs -mcpu=cortex-m4 -mthumb -mfpu=fpv4-sp-d16 -mfloat-abi=softfp" )


#SET(LINKER_SCRIPT_PATH ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32F3/TARGET_STM32F303x8/device/TOOLCHAIN_GCC_ARM/STM32F303X8.ld)
#SET(LINKER_SCRIPT_PATH ${PROJECT_SOURCE_DIR}/mbed-os-example-blinky.link_script.ld)
SET(LINKER_SCRIPT_PATH ${PROJECT_SOURCE_DIR}/mbed-os/targets/TARGET_STM/TARGET_STM32L4/TARGET_STM32L432xC/device/TOOLCHAIN_GCC_ARM/STM32L432XX.ld)


#SET(LD_FLAGS "-Wl,--gc-sections -Wl,--wrap,main -Wl,--wrap,_malloc_r -Wl,--wrap,_free_r -Wl,--wrap,_realloc_r -Wl,--wrap,_calloc_r -Wl,--wrap,exit -Wl,--wrap,atexit -Wl,-n --specs=nano.specs -mcpu=cortex-m4 -mthumb -mfpu=fpv4-sp-d16 -mfloat-abi=softfp -g3 -gdwarf-3 -Os")
#SET(LD_FLAGS "-Wl,--gc-sections -Wl,--wrap,main -Wl,--wrap,_malloc_r -Wl,--wrap,_free_r -Wl,--wrap,_realloc_r -Wl,--wrap,_calloc_r -Wl,--wrap,exit -Wl,--wrap,atexit -Wl,-n")

SET(LD_FLAGS_DEBUG "-Wl,--gc-sections -Wl,--wrap,main -Wl,--wrap,_malloc_r -Wl,--wrap,_free_r -Wl,--wrap,_realloc_r -Wl,--wrap,_calloc_r -Wl,--wrap,exit -Wl,--wrap,atexit -Wl,-n -mcpu=cortex-m4 -mthumb -mfpu=fpv4-sp-d16 -mfloat-abi=softfp")
SET(LD_FLAGS_RELEASE "-Wl,--gc-sections -Wl,--wrap,main -Wl,--wrap,_malloc_r -Wl,--wrap,_free_r -Wl,--wrap,_realloc_r -Wl,--wrap,_calloc_r -Wl,--wrap,exit -Wl,--wrap,atexit -Wl,-n --specs=nano.specs -mcpu=cortex-m4 -mthumb -mfpu=fpv4-sp-d16 -mfloat-abi=softfp -O3")
SET(LD_FLAGS ${LD_FLAGS_RELEASE})



#SET(LD_SYS_LIBS "-Wl,--start-group -lstdc++ -lsupc++ -lm -lc -lgcc -lnosys -Wl,--end-group")
SET(LD_SYS_LIBS "-Wl,--start-group -lstdc++ -lsupc++ -lm -lc -lgcc -lnosys -Wl,--end-group")

# specify the cross compiler
SET(CMAKE_C_COMPILER ${TOOLCHAIN_DIR}/arm-none-eabi-gcc)
SET(CMAKE_CXX_COMPILER ${TOOLCHAIN_DIR}/arm-none-eabi-g++)
SET(CMAKE_ASM_COMPILER ${TOOLCHAIN_DIR}/arm-none-eabi-gcc)


# flags settings
SET(CMAKE_ASM_FLAGS "${ASM_CMD} ${ASMFLGS}")
SET(CMAKE_C_FLAGS "${C_CMD} ${CFLGS}")
SET(CMAKE_CXX_FLAGS "${CXX_CMD} ${CXXFLGS}")

SET(CMAKE_ASM_FLAGS_DEBUG "${ASM_CMD_DEBUG} ${ASMFLGS_DEBUG}")
SET(CMAKE_C_FLAGS_DEBUG "${C_CMD_DEBUG} ${CFLGS_DEBUG}")
SET(CMAKE_CXX_FLAGS_DEBUG "${CXX_CMD_DEBUG} ${CXXFLGS_DEBUG}")

SET(CMAKE_ASM_FLAGS_RELEASE "${ASM_CMD_RELEASE} ${ASMFLGS_RELEASE}")
SET(CMAKE_C_FLAGS_RELEASE "${C_CMD_RELEASE} ${CFLGS_RELEASE}")
SET(CMAKE_CXX_FLAGS_RELEASE "${CXX_CMD_RELEASE} ${CXXFLGS_RELEASE}")

SET(CMAKE_LINK_LIBRARY_FLAG ${LD_SYS_LIBS})
if (CMAKE_BUILD_TYPE EQUAL "Debug")
    message("debug mode")
    SET(CMAKE_EXE_LINKER_FLAGS "${LD_FLAGS_DEBUG} -T${LINKER_SCRIPT_PATH}")
else()
    message("normal mode")
    SET(CMAKE_EXE_LINKER_FLAGS "${LD_FLAGS_RELEASE} -T${LINKER_SCRIPT_PATH}")
endif()

MESSAGE(${CMAKE_ASM_FLAGS})
MESSAGE(${CMAKE_C_FLAGS})
MESSAGE(${CMAKE_CXX_FLAGS})

SET(SOURCE_FILES ${SRCS})
INCLUDE_DIRECTORIES(${INCDIR})

################
# Override the link rules:
set(CMAKE_C_CREATE_SHARED_LIBRARY "echo 'shared libraries not supported' && 1")
set(CMAKE_C_CREATE_SHARED_MODULE  "echo 'shared modules not supported' && 1")
set(CMAKE_C_CREATE_STATIC_LIBRARY "<CMAKE_AR> -cr <LINK_FLAGS> <TARGET> <OBJECTS>")
set(CMAKE_C_COMPILE_OBJECT        "<CMAKE_C_COMPILER> <DEFINES> ${EXPLICIT_INCLUDES}<FLAGS><INCLUDES> -o <OBJECT> -c <SOURCE>")
# <LINK_LIBRARIES> is grouped with system libraries so that system library
# functions (e.g. malloc) can be overridden by symbols in <LINK_LIBRARIES>
#set(CMAKE_C_LINK_EXECUTABLE       "<CMAKE_C_COMPILER> <CMAKE_C_LINK_FLAGS> <LINK_FLAGS> -Wl,-Map,<TARGET>.map -Wl,--start-group <OBJECTS> <LINK_LIBRARIES> ${GLOBALLY_LINKED_TARGET_LIBS} -lm -lc -lgcc -lm -lc -lgcc -Wl,--end-group  --specs=nano.specs -o <TARGET>")
#set(CMAKE_C_LINK_EXECUTABLE       "<CMAKE_C_COMPILER> <CMAKE_C_LINK_FLAGS> <LINK_FLAGS> -Wl,-Map,<TARGET>.map -Wl,--start-group <OBJECTS> <LINK_LIBRARIES> ${GLOBALLY_LINKED_TARGET_LIBS} -lm -lc -lgcc -lm -lc -lgcc -Wl,--end-group -o <TARGET>")
#set(CMAKE_C_LINK_EXECUTABLE       "<CMAKE_C_COMPILER> <CMAKE_C_LINK_FLAGS> <LINK_FLAGS> -Wl,-Map,<TARGET>.map -Wl,--start-group <OBJECTS> <LINK_LIBRARIES> ${GLOBALLY_LINKED_TARGET_LIBS} -lm -lc -lgcc -lm -lc -lgcc -Wl,--end-group -o <TARGET>")

set(CMAKE_C_LINK_EXECUTABLE       "<CMAKE_C_COMPILER> ${LD_FLAGS} -T${LINKER_SCRIPT_PATH} -o <TARGET> <OBJECTS> <LINK_LIBRARIES> ${GLOBALLY_LINKED_TARGET_LIBS} ${LD_SYS_LIBS}")



# set(CMAKE_C_FLAGS_DEBUG_INIT          "-g -gdwarf-3")
# set(CMAKE_C_FLAGS_MINSIZEREL_INIT     "-Os -DNDEBUG")
# set(CMAKE_C_FLAGS_RELEASE_INIT        "-Os -DNDEBUG")
# set(CMAKE_C_FLAGS_RELWITHDEBINFO_INIT "-Os -g -gdwarf-3 -DNDEBUG")
# set(CMAKE_INCLUDE_SYSTEM_FLAG_C "-isystem ")


# set(CMAKE_ASM_FLAGS_DEBUG_INIT          "-g -gdwarf-3")
# set(CMAKE_ASM_FLAGS_MINSIZEREL_INIT     "-Os -DNDEBUG")
# set(CMAKE_ASM_FLAGS_RELEASE_INIT        "-Os -DNDEBUG")
# set(CMAKE_ASM_FLAGS_RELWITHDEBINFO_INIT "-Os -g -gdwarf-3 -DNDEBUG")
# set(CMAKE_INCLUDE_SYSTEM_FLAG_ASM  "-isystem ")


set(CMAKE_CXX_CREATE_SHARED_LIBRARY "echo 'shared libraries not supported' && 1")
set(CMAKE_CXX_CREATE_SHARED_MODULE  "echo 'shared modules not supported' && 1")
set(CMAKE_CXX_CREATE_STATIC_LIBRARY "<CMAKE_AR> -cr <LINK_FLAGS> <TARGET> <OBJECTS>")
set(CMAKE_CXX_COMPILE_OBJECT        "<CMAKE_CXX_COMPILER> <DEFINES> ${EXPLICIT_INCLUDES}<FLAGS><INCLUDES> -o <OBJECT> -c <SOURCE>")
# <LINK_LIBRARIES> is grouped with system libraries so that system library
# functions (e.g. malloc) can be overridden by symbols in <LINK_LIBRARIES>
#set(CMAKE_CXX_LINK_EXECUTABLE       "<CMAKE_CXX_COMPILER> <CMAKE_CXX_LINK_FLAGS> <LINK_FLAGS> -Wl,-Map,<TARGET>.map -Wl,--start-group <OBJECTS> <LINK_LIBRARIES> ${GLOBALLY_LINKED_TARGET_LIBS} -lstdc++ -lsupc++ -lm -lc -lgcc -lstdc++ -lsupc++ -lm -lc -lgcc -Wl,--end-group  --specs=nano.specs -o <TARGET>")
#set(CMAKE_CXX_LINK_EXECUTABLE       "<CMAKE_CXX_COMPILER> <CMAKE_CXX_LINK_FLAGS> <LINK_FLAGS> -Wl,-Map,<TARGET>.map -Wl,--start-group <OBJECTS> <LINK_LIBRARIES> ${GLOBALLY_LINKED_TARGET_LIBS} -lstdc++ -lsupc++ -lm -lc -lgcc -lstdc++ -lsupc++ -lm -lc -lgcc -Wl,--end-group -o <TARGET>")
set(CMAKE_CXX_LINK_EXECUTABLE       "<CMAKE_CXX_COMPILER> ${LD_FLAGS} -T${LINKER_SCRIPT_PATH} -o <TARGET> <OBJECTS> <LINK_LIBRARIES> ${GLOBALLY_LINKED_TARGET_LIBS} ${LD_SYS_LIBS}")



# set(CMAKE_CXX_FLAGS_DEBUG_INIT          "-g -gdwarf-3")
# set(CMAKE_CXX_FLAGS_MINSIZEREL_INIT     "-Os -DNDEBUG")
# set(CMAKE_CXX_FLAGS_RELEASE_INIT        "-Os -DNDEBUG")
# set(CMAKE_CXX_FLAGS_RELWITHDEBINFO_INIT "-Os -g -gdwarf-3 -DNDEBUG")
# set(CMAKE_INCLUDE_SYSTEM_FLAG_CXX "-isystem ")


set(CMAKE_STATIC_LIBRARY_PREFIX "")
set(CMAKE_STATIC_LIBRARY_SUFFIX ".a")
set(CMAKE_EXECUTABLE_SUFFIX "")
set(CMAKE_C_OUTPUT_EXTENSION ".o")
set(CMAKE_ASM_OUTPUT_EXTENSION ".o")
set(CMAKE_CXX_OUTPUT_EXTENSION ".o")

################




#SET(CMAKE_EXE_LINKER_FLAGS "${LD_FLAGS} -T${LINKER_SCRIPT_PATH}")

add_executable(${PROJECT_NAME}.elf ${SOURCE_FILES} ${LINKER_SCRIPT_PATH})

#CMAKE_BINARY_DIR 
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -Wl,-Map=${CMAKE_BINARY_DIR}/${PROJECT_NAME}.map")
set(HEX_FILE ${CMAKE_BINARY_DIR}/${PROJECT_NAME}.hex)
set(BIN_FILE ${CMAKE_BINARY_DIR}/${PROJECT_NAME}.bin)
add_custom_command(TARGET ${PROJECT_NAME}.elf POST_BUILD
        COMMAND ${ELF_CMD} -Oihex $<TARGET_FILE:${PROJECT_NAME}.elf> ${HEX_FILE}
        COMMAND ${ELF_CMD} -Obinary $<TARGET_FILE:${PROJECT_NAME}.elf> ${BIN_FILE}
        COMMENT "Building ${HEX_FILE} \nBuilding ${BIN_FILE}")

#add_executable(${PROJECT_NAME}.elf ${SOURCE_FILES})
#target_link_libraries(${PROJECT_NAME}.elf  ${LD_SYS_LIBS})
