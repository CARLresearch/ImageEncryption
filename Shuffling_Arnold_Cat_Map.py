def transform_ac(img, itr , times_shuffled, p=1,q=1):                                                        #arnold cat map
    n=64
    output_image = np.zeros([64, 64])
    for i in range(times_shuffled):
        for x in range(0, 64):
            for y in range(0, 64):
                output_image[x][y] = img[(x+p*y)%n][(q*x+(p*q+1)*y)%n]
        cv.imwrite('test/'+str(itr).zfill(2)+'_'+str(i).zfill(2)+'.png', output_image)
    cv.imwrite('testfinal/'+str(itr).zfill(2)+'_'+str(i).zfill(2)+'.png', output_image)
    return output_image
